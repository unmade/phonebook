from django.test import TestCase

from rest_framework.test import APITestCase

from .models import Company, Center, Division


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
        сenter126 = Center.objects.get_or_create(
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
            center=сenter126[0],
            number="126-2-1",
            name="Отдел ведения документации"
        )
        division126_2_2 = Division.objects.get_or_create(
            center=сenter126[0],
            number="126-2-2",
            name="Отдел стратегических исследований"
        )
        division126_2_3 = Division.objects.get_or_create(
            center=сenter126[0],
            number="126-2-3",
            name="Отдел наземных комплексов"
        )

        self.company_url = '/api/companies/'
        self.center_url = '/api/centers/'
        self.division_url = '/api/divisions/'

    def test_companies_list(self):
        response = self.client.get(self.company_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'НПОЛ')
        self.assertContains(response, 'НИЦ Планета')
        self.assertEqual(response.data["count"], 2)

    def test_centers_list(self):
        response = self.client.get(self.center_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 126)
        self.assertContains(response, 128)
        self.assertEqual(response.data["count"], 2)

    def test_divisions_list(self):
        response = self.client.get(self.division_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "126-2-1")
        self.assertContains(response, "126-2-2")
        self.assertContains(response, "126-2-3")
        self.assertEqual(response.data["count"], 3)
