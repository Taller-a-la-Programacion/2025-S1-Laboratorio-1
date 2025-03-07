#NO MODIFICAR ESTE ARCHIVO

import Laboratorio01;
import pytest;

    
def test_lab_1():
    assert Laboratorio01.calcularRenta(700000) == 0
    
def test_lab_2():
    assert Laboratorio01.calcularRenta(1000000) == 18300
    
def test_lab_3():
    assert Laboratorio01.calcularRenta(2000000) == 157000
    
def test_lab_4():
    assert Laboratorio01.contadorDigitos(102039480, 0) == 3

def test_lab_5():
    assert Laboratorio01.contadorDigitos(132033483, 3) == 4
    
