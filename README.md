# 大肥鱼·钢盆版

灰蓝长发、银灰钢盆、深色女仆裙和小蓝鲸围裙的自定义桌面宠物，适用于支持 v2 自定义 Pets 的 ChatGPT / Codex 客户端。

完整资源包含 9 组状态动画和 16 个看向不同方向的姿势。鼠标悬停对应的 5 帧使用同一个端盆姿势，避免连续重复端盆动作。

## v1.2.0 更新

- 待机改为端着钢盆吃白饭：舀饭送到嘴边、空勺退开、闭嘴鼓腮咀嚼，再准备下一口。
- 六帧通过勺子、白饭、脸颊和眼睑的变化表达动作，固定头部大小、位置和蓝色头发。
- 仅替换待机行；hover 和其余状态逐像素保持 v1.1.0 原样。

## v1.1.0 更新

- 更新摘盆后的头部绘制，调整头顶弧度，使头型更饱满。
- 将头顶和刘海的偏紫灰色调整为更接近戴盆状态的蓝色。
- 优化白色女仆头饰的连续褶边，补回清楚可见的蓝色呆毛。
- 戴盆待机和其他状态逐像素保持 v1.0.0 原样；hover 仍为 5 帧相同的静止端盆姿势，播放行为没有变化。

## 下载和安装

从 [Releases](https://github.com/1930850328/dafeiyu-pet/releases/latest) 下载 `dafeiyu-pet-v1.2.0.zip`，解压后选择下面一种方式安装。

### 本地桌面宠物

适用于从本地 `pets` 目录读取自定义宠物的客户端，需要 Python 3.8 或更高版本，无须安装第三方依赖。

在解压后的目录运行：

```sh
python3 install.py
```

Windows 可以运行：

```powershell
py -3 install.py
```

脚本将资源复制到 `~/.codex/pets/dafeiyu-steel-basin/`。若设置了 `CODEX_HOME`，则使用该目录下的 `pets/`。已有同名目录时会停止，不覆盖已有宠物；脚本不会修改应用安装包、签名或当前宠物选择。

也可以手动把仓库中的 `pet` 文件夹复制到上述位置并重命名为 `dafeiyu-steel-basin`，确保目录内直接包含 `pet.json` 和 `spritesheet.png`。

安装后打开 **设置 → Pets / Mini 与虚拟宠物**，刷新并选择 **大肥鱼·钢盆版**，再显示宠物。如果列表或图像未更新，可以完全退出应用后重新打开。官方的显示、选择和快捷键说明见 [Pets 文档](https://learn.chatgpt.com/docs/pets)。

需要使用其他宠物目录时：

```sh
python3 install.py --pets-dir /path/to/pets
```

卸载时先切换到其他宠物，再删除 `dafeiyu-steel-basin` 文件夹即可。

### 使用 Pets 插件导入

如果你的客户端使用账号中的 Pets 列表，而不是本地宠物目录，可以把 `pet/spritesheet.png` 附加到一个具备 Pets 插件的对话，发送：

> 请把这张现成的 v2 精灵图导入为我的自定义宠物，名字是“大肥鱼·钢盆版”，描述是“头戴银灰钢盆的DeepSeek大肥鱼，灰蓝长发、深色女仆裙和小蓝鲸围裙。”。沿用原图，校验后上传并选用，不重新生成图片。如果已经有同名宠物，先确认更新对象。

此方法要求账号和插件支持 v2 上传。只接受 `1536 × 1872` 图片的旧版上传入口不能直接导入本仓库的 v2 资源，请使用支持 v2 的客户端。桌面本地安装不会自动同步到网页端。

### 从旧版本更新

本地安装用户先把原有的 `dafeiyu-steel-basin` 文件夹移到 `pets` 目录之外备份，再运行新版的 `install.py`。脚本仍拒绝覆盖已有目录。安装后在设置中刷新并重新选择宠物；若图像仍未更新，完全退出应用后重新打开。

使用账号 Pets 列表的用户，把新版 `pet/spritesheet.png` 交给 Pets 插件，要求更新已有的“大肥鱼·钢盆版”并保留原宠物 ID。请勿重复新建同名宠物。

## 动作说明

| 行（从 0 开始） | 状态 | 有效帧数 |
| --- | --- | ---: |
| 0 | 待机：端盆吃白饭、闭嘴咀嚼 | 6 |
| 1 | 向右移动 | 8 |
| 2 | 向左移动 | 8 |
| 3 | 招手 | 4 |
| 4 | hover / jumping 槽位：静止端盆 | 5 |
| 5 | 失败反馈 | 8 |
| 6 | 等待输入 | 6 |
| 7 | 工作中 | 6 |
| 8 | 检查结果 | 6 |
| 9–10 | 16 个看向不同方向的姿势 | 每行 8 |

当前版本的 hover 会直接切到端盆姿势，没有慢慢端下来的过渡。在发布时检查的桌面播放器中，这组帧总共显示约 2.52 秒后恢复待机；播放过程中移出鼠标会恢复底层状态。持续悬停不会永久保持该姿势。其他客户端的触发方式、时长和状态优先级可能不同，图片资源自身不控制这些行为。

吃饭待机使用 6 帧静态精灵图，播放速度由客户端决定。在本次检查的桌面播放器中，一轮约 6.6 秒。动态 WebP 经账号上传链路保存后会变为单帧 PNG，不能通过这个入口保留额外动画帧；本版本沿用标准 PNG 格式。

## 文件格式

- `pet/spritesheet.png`：完整透明 PNG，`1536 × 2288`，8 列 × 11 行，单帧 `192 × 208`。
- `pet/pet.json`：本地宠物元数据，包含必需的 `spriteVersionNumber: 2`。
- `install.py`：仅使用 Python 标准库的本地安装脚本。
- `SHA256SUMS`：发布文件校验值。

资源已通过 v2 布局校验；吃饭待机与当前账号中已应用的资源逐像素一致，hover 的 5 帧完全相同，非待机行与 v1.1.0 逐像素一致。安装脚本已在临时目录验证复制和拒绝覆盖行为；未宣称在所有客户端或操作系统上完成界面实测。

## 使用许可

本仓库自有内容采用 [MIT License](LICENSE)，允许使用、修改和分享，请保留许可声明。第三方名称和商标不在授权范围内。本项目是社区自定义宠物，与 OpenAI 或 DeepSeek 无官方关联。

## English

Dafeiyu — Steel Basin Edition is a custom v2 pet sprite sheet for compatible ChatGPT / Codex clients. Download the release ZIP, extract it, and run `python3 install.py` (`py -3 install.py` on Windows). Select the pet in Settings → Pets after refreshing. The installer only adds a pet directory and refuses to overwrite an existing one.

The hover row contains five identical basin-holding poses. Playback duration depends on the client; it is not an indefinite hold. The sheet includes nine state rows and sixteen look directions. For account-based Pets, import the unchanged PNG with a v2-capable Pets plugin instead of the local installer.

v1.1.0 updates the uncovered head, blue hair palette, maid headband and ahoge. All non-hover rows are pixel-identical to v1.0.0. To upgrade a local installation, move the old pet directory outside the pets folder as a backup, then run the new installer. For account-based Pets, update the existing pet with the new PNG while retaining its ID.

v1.2.0 replaces only the idle row with a six-frame rice-eating loop: scoop, bring rice to the lips, withdraw the empty spoon, chew with closed lips, and prepare the next bite. Head scale, position and blue hair remain stable. Every non-idle row is pixel-identical to v1.1.0. Timing remains controlled by the client; the inspected desktop player takes about 6.6 seconds per idle loop. The release uses the standard static PNG atlas.
