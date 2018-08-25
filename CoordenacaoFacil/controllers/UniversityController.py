from CoordenacaoFacil import app

@app.route("/app/universities/", methods=["GET"])
def get_all_universities():
    pass


@app.route("/app/universities/<university_id>/", methods=["GET"])
def get_university(university_id):
    pass


@app.route("/app/universities/", methods=["POST"])
def create_university():
    pass


@app.route("/app/universities/<university_id>/", methods=["PUT"])
def update_university(university_id):
    pass


@app.route("/app/universities/<university_id>/", methods=["DELETE"])
def delete_university(university_id):
    pass
