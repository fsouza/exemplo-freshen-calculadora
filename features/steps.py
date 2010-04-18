#coding:utf-8
from freshen import *
from freshen.checks import *
from should_dsl import *
from calculadora import Calculadora

@Before
def criar_calculadora(sc):
    scc.calculadora = Calculadora()

@Given("que eu digitei (\d+) na calculadora")
def digitar_numero(numero):
    scc.calculadora.add_numero(int(numero))

@When("eu aperto o botão de soma")
def somar():
    scc.resultado = scc.calculadora.somar()

@Then("o resultado na calculadora deve ser (\d+)")
def visualizar_resultado(resultado):
    scc.resultado |should_be| int(resultado)
