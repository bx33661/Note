const Book = require("../models/book");
const asyncHandler = require("express-async-handler");

exports.index = asyncHandler(async (req, res, next) => {
  res.send("未实现：网站主页");
});

// 显示所有的图书
exports.book_list = asyncHandler(async (req, res, next) => {
  res.send("未实现：图书列表");
});

// 显示特定图书的详情页面。
exports.book_detail = asyncHandler(async (req, res, next) => {
  res.send(`未实现：图书详情页面：${req.params.id}`);
});

// 通过 GET 显示创建图书。
exports.book_create_get = asyncHandler(async (req, res, next) => {
  res.send("未实现：创建图书 GET");
});

// 以 POST 方式处理创建图书。
exports.book_create_post = asyncHandler(async (req, res, next) => {
  res.send("未实现：Book 创建 POST");
});

// 通过 GET 显示删除图书。
exports.book_delete_get = asyncHandler(async (req, res, next) => {
  res.send("未实现：删除 GET");
});

// 以 POST 方式处理删除图书。
exports.book_delete_post = asyncHandler(async (req, res, next) => {
  res.send("未实现：删除 POST");
});

// 通过 GET 显示更新图书。
exports.book_update_get = asyncHandler(async (req, res, next) => {
  res.send("未实现：更新图书 GET");
});

// 处理 POST 时的更新图书。
exports.book_update_post = asyncHandler(async (req, res, next) => {
  res.send("未实现：更新图书 POST");
});
