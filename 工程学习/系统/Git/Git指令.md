# Git指令

---

GitHub 中的 Git 指令用于在本地和远程仓库之间管理代码和版本控制。以下是一些常用的 Git 指令及其功能介绍：

### 1. **git init**
   初始化一个新的 Git 仓库。这个命令会在当前目录中创建一个 `.git` 文件夹，表示该目录下的所有内容将受 Git 版本控制。
   ```bash
   git init
   ```

### 2. **git clone**
   克隆一个远程仓库到本地。通常用于从 GitHub 上复制现有的项目。
   ```bash
   git clone <repository-url>
   ```

### 3. **git status**
   查看当前工作目录的状态，包括已修改但未提交的文件，未被跟踪的文件等。
   ```bash
   git status
   ```

### 4. **git add**
   将文件添加到暂存区。被添加的文件将包含在下次的提交中。
   ```bash
   git add <file-name>
   ```
   或添加所有更改：
   ```bash
   git add .
   ```

### 5. **git commit**
   提交暂存区的内容到本地仓库。每次提交都会创建一个唯一的快照，包含所有更改的记录。
   ```bash
   git commit -m "commit message"
   ```

### 6. **git push**
   将本地仓库的更改推送到远程仓库。例如将 `main` 分支推送到远程的 `origin` 仓库：
   ```bash
   git push origin main
   ```

### 7. **git pull**
   从远程仓库获取最新的更改，并与本地的分支合并。它相当于运行了 `git fetch` 和 `git merge`。
   ```bash
   git pull origin main
   ```

### 8. **git branch**
   查看当前分支，创建新分支，或删除分支。
   - 查看本地分支：
     ```bash
     git branch
     ```
   - 创建新分支：
     ```bash
     git branch <new-branch-name>
     ```
   - 删除分支：
     ```bash
     git branch -d <branch-name>
     ```

### 9. **git checkout**
   切换到指定的分支或恢复工作目录到指定的提交。
   - 切换分支：
     ```bash
     git checkout <branch-name>
     ```
   - 创建并切换到新分支：
     ```bash
     git checkout -b <new-branch-name>
     ```

### 10. **git merge**
   将另一个分支的更改合并到当前分支。通常用于合并开发分支到主分支。
   ```bash
   git merge <branch-name>
   ```

### 11. **git remote**
   管理远程仓库链接。可以查看已配置的远程仓库，添加新仓库，或者移除仓库。
   - 查看已配置的远程仓库：
     ```bash
     git remote -v
     ```
   - 添加远程仓库：
     ```bash
     git remote add origin <repository-url>
     ```
   - 删除远程仓库：
     ```bash
     git remote remove origin
     ```

### 12. **git log**
   查看提交历史。包括每次提交的哈希值、提交者、日期和提交信息。
   ```bash
   git log
   ```

### 13. **git fetch**
   从远程仓库获取更新但不合并。与 `git pull` 不同，它只下载更改，不会自动将它们合并到当前分支。
   ```bash
   git fetch origin
   ```

### 14. **git rebase**
   重新应用提交，以清理提交历史或避免合并产生的冗余提交。
   ```bash
   git rebase <branch-name>
   ```

### 15. **git reset**
   撤销提交或更改。可以重置文件的暂存状态或将分支重置到之前的状态。
   ```bash
   git reset --hard <commit-hash>
   ```

### 16. **git stash**
   临时存储未完成的工作，以便切换到其他分支或进行其他操作。稍后可以恢复这些更改。
   ```bash
   git stash
   ```
   恢复存储的工作：
   ```bash
   git stash pop
   ```

这些命令组成了 Git 工作流的基础，能够帮助你高效地管理和协作开发项目。