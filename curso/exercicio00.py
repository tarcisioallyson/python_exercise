# Exercício de classes abstratas
from abc import ABC, abstractmethod

class Monitor(ABC):
    def aumentar_claridade(self, tamanho):
        pass
    
    def reduzir_claridade(self, tamanho):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, tamanho):
        print(f'Aumentando a claridade em {tamanho} pontos')

    def reduzir_claridade(self, tamanho):
        print(f'Reduzindo a claridade em {tamanho} pontos')

monitor = MonitorFullHD()
print(monitor.aumentar_claridade(5))
print(monitor.reduzir_claridade(5))