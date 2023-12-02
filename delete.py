import gradio as gr

# Define a function to process text input
def process_text(input_text):
    # Perform some text processing (replace 'a' with 'b' in this example)
    processed_text = input_text.replace('a', 'b')
    return processed_text

# Create a Gradio interface
iface = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(),
    outputs=gr.Textbox(),
    live=True,
    title="Text Processor"
)

# Launch the Gradio interface
iface.launch(share=True)
iface.close()