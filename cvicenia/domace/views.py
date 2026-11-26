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


def du3_teplota(request):
    vysledok = None
    povodna_teplota = ''
    smer = 'c_to_f'

    if request.method == 'POST':
        povodna_teplota = request.POST.get('teplota', '').strip()
        smer = request.POST.get('smer', 'c_to_f')

        try:
            teplota = float(povodna_teplota)

            if smer == 'c_to_f':
                prevedena_teplota = teplota * 9 / 5 + 32
                jednotka = '°F'
            elif smer == 'f_to_c':
                prevedena_teplota = (teplota - 32) * 5 / 9
                jednotka = '°C'
            else:
                raise ValueError('Neplatný smer prevodu.')

            vysledok = f'{prevedena_teplota:.1f} {jednotka}'
        except ValueError:
            vysledok = 'Zadajte platnú číselnú teplotu a vyberte smer prevodu.'

    return render(request, 'domace/du3_teplota.html', {
        'povodna_teplota': povodna_teplota,
        'smer': smer,
        'vysledok': vysledok,
    })
