function getEmployeeList() {
    return {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 4,
                "firstname": "Алексей",
                "patronymic": "Васильевич",
                "surname": "Маслаков",
                "position": "Инженер",
                "company": null,
                "center": null,
                "division": null,
                "phones": [
                    {
                        "id": 1,
                        "category": "Городской",
                        "number": "84955722434",
                        "comment": ""
                    },
                    {
                        "id": 2,
                        "category": "Городской",
                        "number": "84955758013",
                        "comment": ""
                    }
                ],
                "emails": [
                    {
                        "id": 3,
                        "category": "Рабочий",
                        "email": "lesha.maslakov@gmail.com",
                        "comment": ""
                    }
                ],
                "birthday": "1992-09-29",
                "place": "",
                "comment": "",
                "boss": null
            },
            {
                "id": 5,
                "firstname": "Сергей",
                "patronymic": "Антонович",
                "surname": "Лемешевский",
                "position": "И.о. генерального директор",
                "company": {
                    "name": "ФГУП \"НПО им С.А. Лавочкина\"",
                    "url": "/api/companies/2"
                },
                "center": null,
                "division": null,
                "phones": [
                    {
                        "id": 1,
                        "category": "Городской",
                        "number": "84955722434",
                        "comment": ""
                    },
                    {
                        "id": 2,
                        "category": "Городской",
                        "number": "84955758013",
                        "comment": ""
                    },
                    {
                        "id": 3,
                        "category": "Внутренний",
                        "number": "3808",
                        "comment": ""
                    },
                    {
                        "id": 4,
                        "category": "Мобильный",
                        "number": "89067933497",
                        "comment": ""
                    }
                ],
                "emails": [
                    {
                        "id": 1,
                        "category": "Рабочий",
                        "email": "npol@npol.ru",
                        "comment": ""
                    },
                    {
                        "id": 2,
                        "category": "Рабочий",
                        "email": "nkpor@mail.ru",
                        "comment": ""
                    }
                ],
                "birthday": "1952-12-29",
                "place": "",
                "comment": "",
                "boss": null
            },
            {
                "id": 7,
                "firstname": "Василий",
                "patronymic": "Валентинович",
                "surname": "Асмус",
                "position": "Директор",
                "company": {
                    "name": "ФГБУ \"НИЦ \"Планета\"",
                    "url": "/api/companies/3"
                },
                "center": null,
                "division": null,
                "phones": [
                    {
                        "id": 1,
                        "category": "Городской",
                        "number": "84955722434",
                        "comment": ""
                    },
                    {
                        "id": 2,
                        "category": "Городской",
                        "number": "84955758013",
                        "comment": ""
                    }
                ],
                "emails": [],
                "birthday": null,
                "place": "",
                "comment": "",
                "boss": null
            }
        ]
    }
}
