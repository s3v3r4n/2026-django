from django.shortcuts import render


def domace(request):
    ulohy = {
        "uloha1": "uloha prva",
        "uloha2": "uloha druha",
        "uloha3": "uloha tretia",
    }
    return render(request, 'domace/domace.html', ulohy)


def du2_vizitka(request):
    vizitka = {
        'meno': 'Daniel Pokorný',
        'trieda': '3. AT',
        'vek': 17,
        'oblubene_predmety': [
            'Programovanie',
            '3D Modelovanie',
            'Sieťové technológie',
        ],
    }
    vizitka['plnolety'] = vizitka['vek'] >= 18
    return render(request, 'domace/du2_vizitka.html', vizitka)
