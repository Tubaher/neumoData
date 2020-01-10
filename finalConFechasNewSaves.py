import verFechas
import inputs
import shortcuts

inputs.time.sleep(15)
historiasClinicas = []
nPant=1
verFechas.cargarHC(historiasClinicas, "pacfecha.csv")


for hClinic in historiasClinicas:
    shortcuts.entrarHC(hClinic)
    stopExt = True
    ptCounter = 1
    csvFechas = verFechas.extractCSV("pacfecha.csv", hClinic)
    while stopExt:
        screenCp = shortcuts.tomarCaptura(hClinic + str(ptCounter))
        ptCounter += 1
        screenFechas = verFechas.extractFechasScreen(screenCp)
        

        
        for date in csvFechas:
            for i in range(0, len(screenFechas)):
                if screenFechas[i] == date:
                    nPant = shortcuts.recolectarHC(i, hClinic, date, nPant)
        
        for date in screenFechas:
            if int(date[0:4]) <= 2017:
                stopExt = False
                break
        
        if inputs.checkscreen(screenCp) != 0:
            inputs.pulsarTecla(inputs.Key.page_down)
        else:
            stopExt = False
    
    inputs.pulsarTecla(inputs.Key.f3)
    inputs.pulsarTecla(inputs.Key.f3)
    inputs.time.sleep(1)
    
