//wiki路由
const express = require("express")
const router = express.Router()

router.get("/",(req,res)=>{
    res.send("wiki homepage")
})

router.get("/about",(req,res)=>{
    res.send("about wiki")
})

module.exports = router