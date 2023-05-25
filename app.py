import gradio as gr

def function(name, surname):
    
    return "¡Bienvenido!"+ " " +name+ " "+surname

inputs = [
    
    gr.inputs.Textbox(label="Nombre"),
    gr.inputs.Textbox(label="Apellido")
    
]

app = gr.Interface(fn=function, inputs=inputs, outputs="text") 

app.launch()