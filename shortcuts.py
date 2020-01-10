import inputs 

def entrarHC(hClinic):
    inputs.pulsarTecla(inputs.Key.down)
    for i in range(0,8):
        inputs.pulsarTecla(inputs.Key.right)
    for i in range(0,8):
        inputs.pulsarTecla(inputs.Key.backspace)
    inputs.escribir(hClinic)
    inputs.pulsarTecla(inputs.Key.enter)
    inputs.pulsarTeclaDeley(inputs.Key.f11)
    inputs.pulsarTeclaDeley(inputs.Key.f6)

def tomarCaptura(hClinic):
    inputs.pulsarTecla(inputs.Key.alt)
    inputs.pulsarTecla('e')
    inputs.pulsarTecla(inputs.Key.space)
    inputs.time.sleep(1)
    inputs.combTeclas(inputs.Key.ctrl,inputs.Key.tab)
    inputs.pulsarTecla(inputs.Key.enter)
    inputs.escribir(hClinic)
    inputs.pulsarTecla(inputs.Key.enter)
    inputs.combTeclas(inputs.Key.alt, inputs.Key.f4)
    inputs.pulsarTecla(inputs.Key.enter)
    inputs.time.sleep(1)
    return hClinic + '.txt'


def recolectarHC(ind, hClinic, date, nPant):
    for i in range(0, ind):
        inputs.pulsarTecla(inputs.Key.down)
    inputs.pulsarTecla('6')
    inputs.pulsarTeclaDeley(inputs.Key.enter)
    finalFlag = True
    while finalFlag:
        inputs.pulsarTecla(inputs.Key.alt)
        inputs.pulsarTecla('e')
        inputs.pulsarTecla(inputs.Key.space)
        inputs.time.sleep(1)
        inputs.combTeclas(inputs.Key.ctrl,inputs.Key.tab)
        inputs.pulsarTecla(inputs.Key.enter)
        inputs.time.sleep(1)
        ndate = date[0:4] + '-' + date[5:7] + '-' + date[8:10] + '-'
        filename = hClinic + '-' + ndate + str(nPant)
        inputs.escribir(filename)
        inputs.pulsarTecla(inputs.Key.enter)
        inputs.time.sleep(1)
        inputs.combTeclas(inputs.Key.alt, inputs.Key.f4)
        inputs.pulsarTecla(inputs.Key.enter)
        inputs.time.sleep(1)
        #try:
        if inputs.checkscreen(filename) == 0:
           finalFlag = False
        #except:
        #    print("Error")
        #    pass
        #inputs.time.sleep(1)
        inputs.pulsarTecla(inputs.Key.page_down)
        nPant += 1
        inputs.time.sleep(1)
    
    inputs.pulsarTecla(inputs.Key.f3)
    inputs.time.sleep(1)

    return nPant

    
