import nemo.collections.nlp as nemo_nlp
from flask import Flask, render_template, request, jsonify

modelCN = nemo_nlp.models.MTEncDecModel.from_pretrained(model_name="nmt_en_zh_transformer6x6")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html', template_folder='templates')

@app.route("/api", methods=['POST'])
def api():
    source = request.form.get('source')
    translatedText = modelCN.translate([source])
    result = ''.join([str(i) for i in translatedText])
    return jsonify(result)
