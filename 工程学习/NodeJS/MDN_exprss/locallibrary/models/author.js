const mongoose = require("mongoose")
const Schema = mongoose.Schema

const AuthorSchema = new Schema({
    first_name : {type:String,required:true,max:100},
    family_name: {type: String, required: true, maxlength: 100 },
    deta_of_birth:{type:Date},
    data_of_death:{type:Date},
})

AuthorSchema.virtual("name").get(function(){
    return this.famliy_name+","+this.first_name
})

AuthorSchema.virtual("lifespan").get(function(){
    return (
        this.data_of_death.getFullYear(),
        this.deta_of_birth.getFullYear()
    ).toString()
})

AuthorSchema.virtual("url").get(function(){
    return "/catalog/author" + this._id;
})

module.exports = mongoose.model("Author",AuthorSchema)