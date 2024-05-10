Feature: Navegar a la velada del año

  @veladaIV
  Scenario: Velada IV Home Page
    Given Navego a la velada IV
    When Busco el titulo
    Then Valido que sea el canal de Ibai
