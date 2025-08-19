import tkinter as tk #libreria para graficos

root = tk.Tk() #crea la venta
root.title("semaforo")

canvas = tk.Canvas(root, width=1200, height=1200, bg="white") #crea un area para poner cosas
canvas.pack()

#dibuja el semaforo 1
sem1_rojo = canvas.create_oval(50, 30, 100, 80, fill="gray")
sem1_ama = canvas.create_oval(50, 90, 100, 140, fill="gray")
sem1_ver = canvas.create_oval(50, 150, 100, 200, fill="gray")

#dibuja el semaforo 2
sem2_rojo = canvas.create_oval(250, 30, 300, 80, fill="gray")
sem2_ama = canvas.create_oval(250, 90, 300, 140, fill="gray")
sem2_ver = canvas.create_oval(250, 150, 300, 200, fill="gray")

#valores de arranque 
estado = "SEM1_VERDE"
tiempo_boton=0

#colorea los circulos depende de lo que recibe el semaforo1 y semaforo2
def semaforo1(rojo, amarillo, verde):
    canvas.itemconfig(sem1_rojo, fill="red" if rojo else "gray")
    canvas.itemconfig(sem1_ama, fill="yellow" if amarillo else "gray")
    canvas.itemconfig(sem1_ver, fill="green" if verde else "gray")
    
def semaforo2(rojo, amarillo, verde):
    canvas.itemconfig(sem2_rojo, fill="red" if rojo else "gray")
    canvas.itemconfig(sem2_ama, fill="yellow" if amarillo else "gray")
    canvas.itemconfig(sem2_ver, fill="green" if verde else "gray")
    
    

def ciclo():
    global estado, tiempo_boton   #se hace una fuuncion que recibe dos variables glob
    
    if estado == "SEM1_VERDE":        
            semaforo1(0,0,1) #sem1 en verde
            semaforo2(1,0,0) #sem2 en rojo
            estado="SEM1_AMARILLO"
            root.after(5000 + tiempo_boton, ciclo)  #despues de 5 seg ejecuta la ventana
            tiempo_boton= 0
        
    elif estado == "SEM1_AMARILLO":
            semaforo1(0,1,0)                #sem1 en amarillo
            semaforo2(1,0,0)                #sem2 en rojo
            estado = "SEM2_VERDE"
            root.after(2000 ,ciclo)
            tiempo_boton= 0
        
    elif estado == "SEM2_VERDE":
            semaforo1(1,0,0)   #sem1 en rojo
            semaforo2(0,0,1)   #sem2 en verde
            estado= "SEM2_AMARILLO"
            root.after(5000+ tiempo_boton,ciclo)
            
    elif estado == "SEM2_AMARILLO":
            semaforo1(1,0,0)   #sem1 en rojo
            semaforo2(0,1,0)   #sem2 amarillo
            estado= "SEM1_VERDE"
            root.after(2000,ciclo)        
            
def boton1():
    global tiempo_boton
    
    if estado == "SEM1_VERDE" or "SEM2_VERDE":
        tiempo_boton=10000

def boton2():
    global tiempo_boton
    
    if estado == "SEM2_VERDE" or "SEM1_VERDE":
        tiempo_boton=10000
            
            
btn1 = tk.Button(root, text="boton peaton", command= boton1) #al picarle ejecuta lo de command
btn1.pack(side="left", padx=20)

btn2 = tk.Button(root, text="boton peaton2", command=boton2)
btn2.pack(side="right", padx=20)
    

ciclo()
root.mainloop()
