Feature: Navegación en Banistmo

  Scenario: Acceder a la sección de depósitos
    Given el usuario abre el sitio web de Banistmo
    When acepta las cookies
    And navega a la sección de "Cuentas"
    And selecciona "Depósitos"
    And accede a "Cuenta de Ahorro Comercial"
    And abre la pestaña "Tarifario"
    Then la página debe cargar correctamente
