class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        conteo = {}

        for letra in s:
            conteo[letra] = conteo.get(letra, 0) + 1
        
        # Restar caracteres de la segunda cadena
        for letra in t:
            if letra not in conteo or conteo[letra] == 0:
                return False
            conteo[letra] -= 1
            
        return True