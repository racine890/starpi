class api extends Model {
    constructor() {
        super();
        this.id = null;
        this.name = null;
        this.url = null;
        this.method = "GET";
        this.responseType = "Json";
        this.responses = [];
    }
}
