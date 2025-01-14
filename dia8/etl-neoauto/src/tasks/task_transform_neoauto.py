from prefect import task

@task(name="Transformar data de NeoAuto")
def task_transform_neoauto(autos):
    
    autos_transform = []
    
    for auto in autos:
        nombre= auto['nombre']
        url = auto['url']
        precio = auto['precio']
        
        autos_transform.append({
            "nombre": nombre,
            "url": url,
            "precio": float(precio.replace('US$','').replace(',',''))})
        
    return autos_transform