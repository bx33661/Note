const mongoose = require("mongoose")
const Schema = mongoose.Schema


const GenreSchema = new Schema({
    class:{
        type:String,
        requried:true,
        minlength:3,
        maxlength:100
    }
})

GenreSchema.virtual("url").get(function(){
    return `/catalog/genre/${this._id}`
})

module.exports = mongoose.model("Genre",GenreSchema)