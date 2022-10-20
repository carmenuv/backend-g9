class Documento:
  def __init__(self, tipo, num_paginas, editable, contenido):
    # __init__ > será el método que se llame cuando creemos una instancia de la clase
    # en el constructor definimos un nuevo atributo entonces este se creará para toda la clase
    self.tipo = tipo
    self.num_paginas = num_paginas
    self.editable = editable
    self.contenido = contenido

  def editar_documento(self, nuevo_contenido):
    # si el documento no es editable entonces indicar que no se puede editar el documento, caso contrario modificar la información del atributo contenido
    if(self.editable == False):
      print('El archivo no puede ser modificado')
    else:
      self.contenido = nuevo_contenido
      print('El archivo fue modificado a: ' + nuevo_contenido)

mi_curruculum = Documento(tipo='PDF',num_paginas=80, editable=False, contenido='Soy developer')

proforma_pagina_web = Documento(tipo='WORD', num_paginas=3, editable=True, contenido='La página web vale 2500 soles')

mi_curruculum.editar_documento(nuevo_contenido='Ahora soy diseñador')
proforma_pagina_web.editar_documento(nuevo_contenido='La página web vale 4000 soles')