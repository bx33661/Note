const Author = require("../models/author")
const asyncHandler = require("express-async-handler")

exports.author_list = (req,res)=>{
    res.send("pass")
}

exports.author_detail = asyncHandler(async (req,res,next)=>{
    res.send("pass"+req.params.id)
})

exports.author_create_get = asyncHandler(async (req,res,next)=>{
    res.send("pass")
})

exports.author_create_post = asyncHandler(async (req,res,next)=>{
    res.send("pass")
})

exports.author_delete_get = asyncHandler(async (req, res, next) => {
    res.send("未实现：删除作者的 GET");
  });
  
  // 由 POST 处理作者删除操作
  exports.author_delete_post = asyncHandler(async (req, res, next) => {
    res.send("未实现：删除作者的 POST");
});
  
  // 由 GET 显示更新作者的表单
  exports.author_update_get = asyncHandler(async (req, res, next) => {
    res.send("未实现：更新作者的 GET");
  });
  
  // 由 POST 处理作者更新操作
  exports.author_update_post = asyncHandler(async (req, res, next) => {
    res.send("未实现：更新作者的 POST");
  });