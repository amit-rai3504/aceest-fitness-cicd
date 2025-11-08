from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "service": "aceest-fitness"}), 200

    @app.get("/")
    def root():
        return jsonify({"message": "ACEest Fitness API", "version": "v1"}), 200

    # Example domain stub (replace with real logic later)
    @app.get("/members")
    def list_members():
        # Stub data for demo/testing
        return jsonify({"members": [{"id": 1, "name": "Alex"}, {"id": 2, "name": "Sam"}]}), 200

    @app.post("/members")
    def create_member():
        data = request.get_json(silent=True) or {}
        if "name" not in data or not data["name"]:
            return jsonify({"error": "name is required"}), 400
        # In a real app insert into DB; here echo back
        return jsonify({"id": 99, "name": data["name"]}), 201

    return app
