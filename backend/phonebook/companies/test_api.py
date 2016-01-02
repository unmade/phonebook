import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework.test import APITestCase

from .models import Company, Center, Division
from .serializers import CompanySerializer, CenterSerializer, DivisionSerializer


class CompaniesTests(TestCase):
    def setUp(self):
        npol = Company.objects.get_or_create(
            name='ФГУП "НПО им. С.А. Лавочкина"',
            full_name='Федеральное государственное унитарное предприятие\
                       "Научно-производственное объединение имени С. А. Лавочкина',
            short_name='НПОЛ',
            address='141401, г. Химки, Ленинградское шоссе, д.24'
        )
        planet = Company.objects.get_or_create(
            name='ФГБУ "НИЦ "Планета"',
            full_name='Федеральное государственное бюджетное учреждение\
                       "Научно-исследовательский центр космической гидрометеорологии "Планета"',
            short_name='НИЦ Планета',
            address='123242, г. Москва, Большой Предтеченский пер., д.7'
        )
        center126 = Center.objects.get_or_create(
            company=npol[0],
            number=126,
            name="Центр целевых комплексов"
        )
        сenter128 = Center.objects.get_or_create(
            company=npol[0],
            number=128,
            name="Центр управления МКА ФКИ"
        )
        division126_2_1 = Division.objects.get_or_create(
            center=center126[0],
            number="126-2-1",
            name="Отдел ведения документации"
        )
        division126_2_2 = Division.objects.get_or_create(
            center=center126[0],
            number="126-2-2",
            name="Отдел стратегических исследований"
        )
        division126_2_3 = Division.objects.get_or_create(
            center=center126[0],
            number="126-2-3",
            name="Отдел наземных комплексов"
        )

        self.serialized_company = CompanySerializer(npol[0])
        self.serialized_center = CenterSerializer(center126[0])
        self.serialized_division = DivisionSerializer(division126_2_3[0])

        self.companies_list_url = reverse('api:company-list')
        self.centers_list_url = reverse('api:center-list')
        self.divisions_list_url = reverse('api:division-list')

        self.company_detail_url = reverse('api:company-detail', kwargs={'pk': npol[0].pk})
        self.center_detail_url = reverse('api:center-detail', kwargs={'pk': center126[0].pk})
        self.division_detail_url = reverse('api:division-detail', kwargs={'pk': division126_2_3[0].pk})

    def test_companies_list(self):
        response = self.client.get(self.companies_list_url)
        self.assertContains(response, 'НПОЛ')
        self.assertContains(response, 'НИЦ Планета')
        self.assertEqual(response.data["count"], 2)

    def test_company_detail(self):
        response = self.client.get(self.company_detail_url)
        data = json.loads(response.content.decode())
        data["logo"] = "/media/logos/no-logo.png"
        self.assertEquals(data, self.serialized_company.data)

    def test_centers_list(self):
        response = self.client.get(self.centers_list_url)
        self.assertContains(response, 126)
        self.assertContains(response, 128)
        self.assertEqual(response.data["count"], 2)

    def test_center_detail(self):
        response = self.client.get(self.center_detail_url)
        data = json.loads(response.content.decode())
        self.assertEquals(data, self.serialized_center.data)

    def test_divisions_list(self):
        response = self.client.get(self.divisions_list_url)
        self.assertContains(response, "126-2-1")
        self.assertContains(response, "126-2-2")
        self.assertContains(response, "126-2-3")
        self.assertEqual(response.data["count"], 3)

    def test_division_detail(self):
        response = self.client.get(self.division_detail_url)
        data = json.loads(response.content.decode())
        self.assertEquals(data, self.serialized_division.data)
