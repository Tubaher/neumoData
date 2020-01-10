import verFechas
import inputs
import shortcutsNewSaves

inputs.time.sleep(15)
historiasClinicas = []
verFechas.cargarHC(historiasClinicas, "pacfecha.csv")


for hClinic in historiasClinicas:
    shortcutsNewSaves.entrarHC(hClinic)
    stopExt = True
    ptCounter = 1
    csvFechas = verFechas.extractCSV("pacfecha.csv", hClinic)
    while stopExt:
        screenCp = shortcutsNewSaves.tomarCaptura(hClinic + str(ptCounter))
        
        screenFechas = verFechas.extractFechasScreen(screenCp)
        

        
        for date in csvFechas:
            nFechRep = 1
            for i in range(0, len(screenFechas)):
                if screenFechas[i] == date:
                    shortcutsNewSaves.recolectarHC(i, hClinic, date, ptCounter, nFechRep)
                    nFechRep += 1
        
        for date in screenFechas:
            if int(date[0:4]) <= 2017:
                stopExt = False
                break
        
        if inputs.checkscreen(screenCp) != 0:
            inputs.pulsarTecla(inputs.Key.page_down)
        else:
            stopExt = False
        ptCounter += 1
    inputs.combTeclas(inputs.Key.f3,inputs.Key.f3)
    inputs.pulsarTecla(inputs.Key.f3)
    inputs.pulsarTecla(inputs.Key.f3)
    inputs.time.sleep(1)
    
