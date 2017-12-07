import json

from django.test import TestCase
from django.urls import reverse

from .models import Center, Company, Division
from .serializers import CenterSerializer, CompanySerializer, DivisionSerializer


class CompaniesTests(TestCase):
    def setUp(self):
        self.company, _ = Company.objects.get_or_create(
            name='ФГУП "НПО им. С.А. Лавочкина"',
            full_name=(
                'Федеральное государственное унитарное предприятие'
                '"Научно-производственное объединение имени С. А. Лавочкина',
            ),
            short_name='НПОЛ',
            address='141401, г. Химки, Ленинградское шоссе, д.24'
        )
        Company.objects.get_or_create(
            name='ФГБУ "НИЦ "Планета"',
            full_name='Федеральное государственное бюджетное учреждение\
                       "Научно-исследовательский центр космической гидрометеорологии "Планета"',
            short_name='НИЦ Планета',
            address='123242, г. Москва, Большой Предтеченский пер., д.7'
        )

        self.center, _ = Center.objects.get_or_create(
            company=self.company,
            number=126,
            name='Центр целевых комплексов'
        )
        Center.objects.get_or_create(
            company=self.company,
            number=128,
            name='Центр управления МКА ФКИ'
        )

        self.division, _ = Division.objects.get_or_create(
            center=self.center,
            number='126-2-3',
            name='Отдел наземных комплексов'
        )
        Division.objects.get_or_create(
            center=self.center,
            number='126-2-1',
            name='Отдел ведения документации'
        )
        Division.objects.get_or_create(
            center=self.center,
            number='126-2-2',
            name='Отдел стратегических исследований'
        )

    def test_companies_list(self):
        url = reverse('companies:api:company-list')
        response = self.client.get(url)
        self.assertContains(response, 'НПОЛ')
        self.assertContains(response, 'НИЦ Планета')
        self.assertEqual(response.data['count'], 2)

    def test_company_detail(self):
        url = reverse('companies:api:company-detail', kwargs={'pk': self.company.pk})
        response = self.client.get(url)
        data = json.loads(response.content.decode())
        data['logo'] = '/media/logos/no-logo.png'
        self.assertEqual(data, CompanySerializer(self.company).data)

    def test_centers_list(self):
        url = reverse('companies:api:center-list')
        response = self.client.get(url)
        self.assertContains(response, 126)
        self.assertContains(response, 128)
        self.assertEqual(response.data['count'], 2)

    def test_center_detail(self):
        url = reverse('companies:api:center-detail', kwargs={'pk': self.center.pk})
        response = self.client.get(url)
        data = json.loads(response.content.decode())
        self.assertEqual(data, CenterSerializer(self.center).data)

    def test_divisions_list(self):
        url = reverse('companies:api:division-list')
        response = self.client.get(url)
        self.assertContains(response, '126-2-1')
        self.assertContains(response, '126-2-2')
        self.assertContains(response, '126-2-3')
        self.assertEqual(response.data['count'], 3)

    def test_division_detail(self):
        url = reverse('companies:api:division-detail', kwargs={'pk': self.division.pk})
        response = self.client.get(url)
        data = json.loads(response.content.decode())
        self.assertEqual(data, DivisionSerializer(self.division).data)
