![[Pasted image 20240821110110.png]]
1. 使用GET方式传参数
![[Pasted image 20240821110224.png]]
2. 使用POST传参数
```html
<!-- Secret: base64_decode(bjN3c3Q0ckNURjIwMjNnMDAwMDBk) -->
```
使用base64解码，得到值为`n3wst4rCTF2023g00000d`
3. 修改cookie中的power量为`ctfer`
4. ![[Pasted image 20240821110636.png]]
修改UA值为`# NewStarCTF2023`
5. ![[Pasted image 20240821110714.png]]
添加`referer`值为`# newstarctf.com`
6. ![[Pasted image 20240821110801.png]]
添加XFF，发现不行，添加别的形式
7. 得到flag
![[Pasted image 20240821111018.png]]