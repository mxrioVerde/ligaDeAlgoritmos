with open('input.txt') as f:
    caminho = f.read().splitlines()

def caminhante(cam):
    def backtrack(index, _cam):
        camC = _cam.replace(',', '')
        tamA = int(camC[index])
        casaP = index + tamA

        #caso base, fim do array
        if casaP >= len(camC) - 1:
            return True
        
        #caso base, fim das possibilidades de teste
        if tamA == 0:
            return False
        
        for passo in range(1, tamA + 1):
            proxima = index + passo
            if proxima < len(camC):
                if backtrack(proxima, camC):
                    return True

        return False
    
    return True if backtrack(0, cam) else False

ans = 1
for i in range(len(caminho)):
    if not caminhante(caminho[i]):
        ans = ans * (i + 1)

print(ans % (10**9 + 7))