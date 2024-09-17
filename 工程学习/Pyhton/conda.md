## conda

Conda 是一个开源的包管理系统和环境管理系统，主要用于 Python 编程，但也可以打包和分发其他语言的软件。以下是 Conda 的基本使用方法：

1. 安装 Conda
   - 下载并安装 Miniconda 或 Anaconda

2. 创建环境
   ```
   conda create --name myenv python=3.8
   ```
   这会创建一个名为 myenv 的环境，使用 Python 3.8

3. 激活环境
   ```
   conda activate myenv
   ```

4. 停用环境
   ```
   conda deactivate
   ```

5. 列出所有环境
   ```
   conda env list
   ```

6. 安装包
   ```
   conda install numpy
   ```

7. 卸载包
   ```
   conda remove numpy
   ```

8. 更新包
   ```
   conda update numpy
   ```

9. 列出已安装的包
   ```
   conda list
   ```

10. 搜索可用包
    ```
    conda search scipy
    ```

11. 导出环境
    ```
    conda env export > environment.yml
    ```

12. 从文件创建环境
    ```
    conda env create -f environment.yml
    ```

13. 删除环境
    ```
    conda env remove --name myenv
    ```

14. 更新 Conda 自身
    ```
    conda update conda
    ```

15. 清理不再使用的包和缓存
    ```
    conda clean -a
    ```

16. 添加 Conda 频道
    ```
    conda config --add channels conda-forge
    ```

记住，在使用 Conda 时，最好在虚拟环境中工作，这样可以避免影响系统级的 Python 安装。通过为每个项目创建单独的环境，你可以更好地管理依赖关系，并确保项目的可移植性。