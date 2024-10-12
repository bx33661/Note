const genre = require("../models/genre");
const asyncHandler = require("express-async-handler");

// 显示所有的流派。
exports.genre_list = asyncHandler(async (req, res, next) => {
  res.send("未实现：流派列表");
});

// 显示特定流派的详情页。
exports.genre_detail = asyncHandler(async (req, res, next) => {
  res.send(`未实现：流派详情页：${req.params.id}`);
});

// 通过 GET 显示创建流派。
exports.genre_create_get = asyncHandler(async (req, res, next) => {
  res.send("未实现：流派创建 GET");
});

// 以 POST 方式处理创建流派。
exports.genre_create_post = asyncHandler(async (req, res, next) => {
  res.send("未实现：流派创建 POST");
});

// 通过 GET 显示流派删除表单。
exports.genre_delete_get = asyncHandler(async (req, res, next) => {
  res.send("未实现：流派删除 GET");
});

// 处理 POST 时的流派删除。
exports.genre_delete_post = asyncHandler(async (req, res, next) => {
  res.send("未实现：流派删除 POST");
});

// 通过 GET 显示流派更新表单。
exports.genre_update_get = asyncHandler(async (req, res, next) => {
  res.send("未实现：流派更新 GET");
});

// 处理 POST 上的流派更新。
exports.genre_update_post = asyncHandler(async (req, res, next) => {
  res.send("未实现：流派更新 POST");
});
