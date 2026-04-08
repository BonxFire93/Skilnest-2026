# Define la clase SuscripcionStreaming, que debe incluir:

# Atributos:
# usuario (nombre del usuario asociado a la suscripción)
# tipo_suscripcion (Gratis, Estándar, Premium)
# costo_mensual (según el tipo de suscripción)
# saldo_pendiente (monto acumulado que debe pagar el usuario)
# Métodos:
# realizar_pago(self, monto) reduce el saldo pendiente según el monto pagado.
# cambiar_suscripcion(self, nuevo_tipo) cambia el tipo de suscripción y ajusta el costo mensual.
# ver_contenido_exclusivo(self) permite el acceso a contenido según el tipo de suscripción. La suscripción “Gratis” no tiene acceso a contenido exclusivo.
# mostrar_info_suscripcion(self) muestra el estado actual de la suscripción del usuario.
#  Realizar las siguientes pruebas con instancias:

# Crea 3 usuarios con diferentes tipos de suscripción.
# Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
# Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
# Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.

class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion, costo_mensual=0, saldo_pendiente=0):
        self.sus = usuario
        self.tip_sub = tipo_suscripcion
        self.cos_men = self.costos_suscripcion[self.tip_sub]
        self.sal_pen = saldo_pendiente

    def realizar_pago(self, monto):
        self.sal_pen += self.cos_men
        if monto > 0:
            self.sal_pen = max(0, self.sal_pen - monto)

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.costos_suscripcion:
            self.tip_sub = nuevo_tipo
            self.cos_men = self.costos_suscripcion[nuevo_tipo]

    def ver_contenido_exclusivo(self):
        return self.tip_sub != "Gratis"

    def mostrar_info_suscripcion(self):
        print(self.sus, self.tip_sub, self.cos_men, round(self.sal_pen, 2))