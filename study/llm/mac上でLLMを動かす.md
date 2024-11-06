start：[[2023-08-27]] 15:11

### Rinna malc-llm

- [rinna/japanese-gpt-neox-3.6b-instruction-ppo · Hugging Face](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo)
- [GitHub - mlc-ai/mlc-llm: Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.](https://github.com/mlc-ai/mlc-llm)
  - Llama や Vicuna をいろいろな環境で動かす仕組み
- [GitHub - mlc-ai/web-llm: Bringing large-language models and chat to web browsers. Everything runs inside the browser with no server support.](https://github.com/mlc-ai/web-llm/tree/main?tab=readme-ov-file)
  - LLM を web browser として動かす
- [WebLLM | Home](https://webllm.mlc.ai/)
  - [Try out MLC Chat — mlc-llm 0.1.0 documentation](https://mlc.ai/mlc-llm/docs/get_started/try_out.html)

メリット

- mac で rinna が動く
- cli でチャットや python で動作する
  デメリット
- 少しカスタマイズがしずらい
- 少し導入が面倒
- リクエストを飛ばせる感じの実装はされていない

### LLaMA.cpp

- [GPT-3 のライバルとなる Meta の「LLaMA」を M1 搭載 Mac で実行可能に、大規模言語モデルを普通の消費者向けハードウェアで実行可能であることが示される - GIGAZINE](https://gigazine.net/news/20230313-llama-on-m1-mac/)
- [GitHub - ggerganov/llama.cpp: Port of Facebook's LLaMA model in C/C++](https://github.com/ggerganov/llama.cpp)
- [GitHub - ggerganov/whisper.cpp: Port of OpenAI's Whisper model in C/C++](https://github.com/ggerganov/whisper.cpp)
- [l1x/dev | Using LLaMA with M1 Mac](https://dev.l1x.be/posts/2023/03/12/using-llama-with-m1-mac/)
- [Save bandwidth by using a torrent to distribute more efficiently by ChristopherKing42 · Pull Request #73 · facebookresearch/llama · GitHub](https://github.com/facebookresearch/llama/pull/73)
- [Llama.cpp で Llama 2 を試す｜ npaka](https://note.com/npaka/n/n0ad63134fbe2)
- [llama.cpp - Google 検索](https://www.google.com/search?q=llama.cpp&oq=llama.cpp&aqs=chrome..69i57j69i60l2j69i61.4095j0j1&sourceid=chrome&ie=UTF-8)
- [GitHub - abetlen/llama-cpp-python: Python bindings for llama.cpp](https://github.com/abetlen/llama-cpp-python)
- [llama.cpp で CPU で LLM のメモ(2023/05/15 時点日本語もいけるよ)](https://zenn.dev/syoyo/articles/f869a3fda15f45)

一度 mac 上で cpp を build するかんじ

メリット

- mac で動かせる
- whisper.cpp も動かせるかも
- mac での動作が公式でサポートされていて面倒でない
- Docker とか color とかもサポートしている...
  - [ ] [GitHub - ggerganov/llama.cpp: Port of Facebook's LLaMA model in C/C++](https://github.com/ggerganov/llama.cpp#docker)
- GPT4ALL とか llama v2 にもサポートしてる - いろんなモデルを軽量でサポートしている
  デメリット
- llama なので日本語は非対応
- 大きそう

#### npaka さんの記事で導入 ✅

- [Llama.cpp で Llama 2 を試す｜ npaka](https://note.com/npaka/n/n0ad63134fbe2)

```json
**・依存関係のないプレーンなC/C++実装
・Appleシリコンファースト** (ARM NEON、Accelerate、Metalを介して最適化)**
・x86アーキテクチャのAVX、AVX2、AVX512のサポート
・Mixed F16/F32精度
・4bit、5bit、8bit量子化サポート
・BLASでOpenBLAS/Apple BLAS/ARM Performance Lib/ATLAS/BLIS/Intel MKL/NVHPC/ACML/SCSL/SGIMATHなどをサポート
・cuBLASとCLBlastのサポート**
```

- Docker サポート

1. 4bit 量子化版「[**llama-2-7b-chat.ggmlv3.q4_K_M.bin**](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_K_M.bin)」ダウンロード
2. Xcode が入っているか確認 1. `xcode-select -p`
   ![[Pasted image 20230827204931.png]]

3. llama.cpp の実行

```sh
pwd # /Users/takeshitashunji/Programming/Python/py_study
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# build
make

# ダウンロードしたモデルをllama.cpp/models下へ配置

# 推論実行
~~$ ./main -m ./models/llama-2-7b-chat.ggmlv3.q4_K_M.bin --temp 0.1 -p "### Instruction: What is the height of Mount Fuji? ### Response:"~~

# 最新バージョンでggml-> ggufへ変更
# 下記convertで変換
$ ./main -m ./models/llama-2-7b-chat.ggmlv3.q4_K_M.bin --temp 0.1 -p "### Instruction: What is the height of Mount Fuji? ### Response:"


```

エラー解決できなかった

- モデルのダウンロードが悪いのか k な
- llama cpp python があるのでそっちを使う

モデル変換後できた

### llama-cpp-python ✅

- [Llama.cpp で Llama 2 を試す｜ npaka](https://note.com/npaka/n/n0ad63134fbe2)
- [GitHub - abetlen/llama-cpp-python: Python bindings for llama.cpp](https://github.com/abetlen/llama-cpp-python)

```python
mkdir llama-cpp-python
cd llama-cpp-python
conda create -n llama-cpp-python python=3.9
conda activate llama-cpp-python
which python
pip install -U pip
pip install llama-cpp-python # convertしないならバージョンを1.79とかに下げる

vi hello_ggml.py
python hello_ggml.py
```

- hello_ggml.py

```python
from llama_cpp import Llama
import os

# モデルの指定
model = "../llama.cpp/models/llama-2-7b-chat.ggmlv3.q4_K_M.gguf"
if not os.path.exists(model):
    raise FileNotFoundError(f"{model} not found.")

# LLMの準備
llm = Llama(model_path=model)

# プロンプトの準備
prompt = """### Instruction: What is the height of Mount Fuji?
### Response:"""

# 推論の実行
output = llm(
    prompt,
    temperature=0.1,
    stop=["Instruction:", "Input:", "Response:", "\n"],
    echo=True,
)
print(output["choices"][0]["text"])

```

やはりモデルでエラーだな
それか conda で仮想環境を作るべきか

> Starting with version 0.1.79 the model format has changed from `ggmlv3` to `gguf`. Old model files can be converted using the `convert-llama-ggmlv3-to-gguf.py` script in [`llama.cpp`](https://github.com/ggerganov/llama.cpp)

-> サポートするモデル format が変化したらしい、convert してみる

- [GitHub - ggerganov/llama.cpp: Port of Facebook's LLaMA model in C/C++](https://github.com/ggerganov/llama.cpp#prepare-data--run)

convert したら返答が返ってきた.
日本語応答は弱め？

#### モデルを gguf にコンバート ✅

```sh
conda info -e
conda create -n llama.cpp python=3.9
conda activate llama.cpp
pip install -U pip
pip install -r requirements.txt
python convert-llama-ggmlv3-to-gguf.py models/llama-2-7b-chat.ggmlv3.q4_K_M.bin
python convert-llama-ggmlv3-to-gguf.py -i models/llama-2-7b-chat.ggmlv3.q4_K_M.bin -o models/llama-2-7b-chat.ggmlv3.q4_K_M.gguf  --eps 1e-5 -c 4096
```

- 最後の bin-> gguf のスクリプトの正解
  - [Silently failing ggml to gguf conversion · Issue #2697 · ggerganov/llama.cpp · GitHub](https://github.com/ggerganov/llama.cpp/issues/2697)
  - 全体：[GitHub - ggerganov/llama.cpp: Port of Facebook's LLaMA model in C/C++](https://github.com/ggerganov/llama.cpp#prepare-data--run)

### llama.cpp Vicuna

- [llama.cpp で CPU で LLM のメモ(2023/05/15 時点日本語もいけるよ)](https://zenn.dev/syoyo/articles/f869a3fda15f45)
  - 日本語もいけるとのことで導入してみたい

#### モデルダウンロード&実行テスト

1. ~~[eachadea/ggml-vicuna-7b-1.1 at main](https://huggingface.co/eachadea/ggml-vicuna-7b-1.1/tree/main)~~ [TheBloke/vicuna-7B-v1.3-GGML at main](https://huggingface.co/TheBloke/vicuna-7B-v1.3-GGML/tree/main): から `~-7b-q4_0.bin`をダウンロード

2. 実行(text generation)

```python
# モデルを配置
mv models/vicuna-7b-v1.3.ggmlv3.q4_0.bin /Users/takeshitashunji/Programming/Python/py_study/llama.cpp/models/

# convert
conda activate llama.cpp
python convert-llama-ggmlv3-to-gguf.py -i models/vicuna-7b-v1.3.ggmlv3.q4_0.bin -o models/vicuna-7b-v1.3.ggmlv3.q4_0.gguf --eps 1e-5 -c 4096

# 実行(text generation)
./main -m models/vicuna-7b-v1.3.ggmlv3.q4_0.gguf --temp 0.1 -p "### Instruction: What is the height of Mount Fuji? ### Response:"
# -iをつけるとinterractive modeになる -iオプションは変になるからいいかな...

# 実行(日本語, text generation)
./main -m models/vicuna-7b-v1.3.ggmlv3.q4_0.gguf --temp 0.1 -p "### Instruction:富士山の高さは？ ### Response:"
```

英語だとちゃんと返信が返ってきた

日本語は内容が怪しくずっと同じことを繰り返しており中断した
しかし、日本語は帰ってきていた

##### モデルが ggmlv3 にする必要がある

GGJTV3 出ないので convert できないらしい

-> vicuna の ggml verison を取得する

- [TheBloke/vicuna-7B-v1.3-GGML at main](https://huggingface.co/TheBloke/vicuna-7B-v1.3-GGML/tree/main): Huggingface にある
- [TheBloke/vicuna-13B-v1.5-16K-GGML at main](https://huggingface.co/TheBloke/vicuna-13B-v1.5-16K-GGML/tree/main): 色々な vicuna がある
- エラー詳細：[Anyone keeping tabs on Vicuna, a new LLaMA-based model? · ggerganov/llama.cpp · Discussion #643 · GitHub](https://github.com/ggerganov/llama.cpp/discussions/643#discussioncomment-5533894)
  - 対応策も

新しく ggmlv3 のモデルを convert したらできた。13B も同様

3. ~~[eachadea/ggml-vicuna-13b-1.1 at main](https://huggingface.co/eachadea/ggml-vicuna-13b-1.1/tree/main)~~ [TheBloke/vicuna-13B-v1.5-16K-GGML at main](https://huggingface.co/TheBloke/vicuna-13B-v1.5-16K-GGML/tree/main)から `~13b-q4_0.bin`をダウンロード

4. 実行(chat mode)
   1. [GitHub - ggerganov/llama.cpp: Port of Facebook's LLaMA model in C/C++](https://github.com/ggerganov/llama.cpp#interactive-mode)
   2.

```python
# モデルを配置
mv ggml-vicuna-13b-q4_0.bin /Users/takeshitashunji/Programming/Python/py_study/llama.cpp/models/

# convert
conda activate llama.cpp
python convert-llama-ggmlv3-to-gguf.py -i models/vicuna-13b-v1.5-16k.ggmlv3.q4_0.bin -o models/vicuna-13b-v1.5-16k.ggmlv3.q4_0.gguf --eps 1e-5 -c 4096

# 実行(text generation)
./main -m models/vicuna-13b-v1.5-16k.ggmlv3.q4_0.gguf --temp 0.1 -p "### Instruction: What is the height of Mount Fuji? ### Response:"

# 実行(日本語, text chat mode)
./main -m models/vicuna-13b-v1.5-16k.ggmlv3.q4_0.gguf --temp 0.1 -p "### Instruction:富士山の高さは？ ### Response:"
```

英語で 13B に質問すると間違ってる回答多め?
なんか終わり側がわからない感じか

Chat mode Example
[GitHub - ggerganov/llama.cpp: Port of Facebook's LLaMA model in C/C++](https://github.com/ggerganov/llama.cpp#interactive-mode)
これも同じことしてる

- [Anyone keeping tabs on Vicuna, a new LLaMA-based model? · ggerganov/llama.cpp · Discussion #643 · GitHub](https://github.com/ggerganov/llama.cpp/discussions/643#discussioncomment-5589738)
  1 . ここのテキストを prompt 下にコピー
  [Anyone keeping tabs on Vicuna, a new LLaMA-based model? · ggerganov/llama.cpp · Discussion #643 · GitHub](https://github.com/ggerganov/llama.cpp/discussions/643#discussioncomment-5530637)

```txt
A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.

### Human: Hello, Assistant.
### Assistant: Hello. How may I help you today?
### Human: Please tell me the largest city in Europe.
### Assistant: Sure. The largest city in Europe is Moscow, the capital of Russia.
### Human:
```

```python
# 7B
./main -m ./models/vicuna-7b-v1.3.ggmlv3.q4_0.gguf -n 256 --repeat_penalty 1.1 --color -i -r "### Human:" -f prompts/chat-with-vicuna.txt

#7B 少し使いやすい
./main -m ./models/vicuna-7b-v1.3.ggmlv3.q4_0.gguf -n 256 --repeat_penalty 1.1 --color -i -r "##"

#13B
./main -m ./models/vicuna-13b-v1.5-16k.ggmlv3.q4_0.gguf -n 256 --repeat_penalty 1.1 --color -i -r "### Human:" -f prompts/chat-with-vicuna.txt
```

結構返答も遅い?

- 内容は明るめで面白い

vicuna は日本語に対応したモデル

- LLaMA とか Alpaca とかと肩を並べる

- [x] https://zenn.dev/kkatsuyoshi/articles/916ae1db24c9ec | rinna-3.6b を mlc-llm を使って Mac で動かす
- [x] https://www.google.com/search?q=mac+llm&oq=mac+llm&aqs=chrome.0.69i59j69i64j0i4i30j0i8i30l4j69i61.1512j0j1&sourceid=chrome&ie=UTF-8#ip=1 | mac llm - Google 検索
- [x] https://gigazine.net/news/20230313-llama-on-m1-mac/ | GPT-3 のライバルとなる Meta の「LLaMA」を M1 搭載 Mac で実行可能に、大規模言語モデルを普通の消費者向けハードウェアで実行可能であることが示される - GIGAZINE
- [x] https://digitallife.tokyo/archives/2023/08/apple-m1-macbook-pro-local-chatgpt-like-llm-meta-llama-2-install-text-generation-web-ui.html | Apple M1 MacBook Pro ローカルに ChatGPT ライクな LLM Meta Llama 2 を簡単インストールする方法 #textgenerationwebui #ChatGPT #Llama2 | Digital Life Innovator
- [ ] https://blog.hapins.net/entry/2023/03/29/080347 | Mac で動く LLM の Alpaca.cpp - HapInS Developers Blog
- [ ] https://note.com/kotatsurin/n/nc93d736cdc8f | 大規模言語モデル OPT を M1/M2 Mac 上の FlexGen で動かしてチャットする｜りん こうたつ
- [ ] https://simonwillison.net/2023/Aug/1/llama-2-mac/ | Run Llama 2 on your own Mac using LLM and Homebrew
- [ ] https://llcc.hatenablog.com/entry/2023/05/20/225822 | Mac でサイバーエージェントの公開した LLM を動かしてみる - しめ鯖日記
- [ ] https://www.docswell.com/s/karaage0703/Z38EP1-2023-07-19-201446 | オープンな LLM をローカルで動かす | ドクセル
- [ ] https://pc.watch.impress.co.jp/docs/column/nishikawa/1519390.html | 【西川和久の不定期コラム】LLM がローカルで動くパラメータ数どこまで？Meta の「Llama 2」を試してみた - PC Watch
- [ ] https://article.auone.jp/detail/1/3/7/48_7_r_20230313_1678690803733329 | GPT-3 のライバルとなる Meta の「LLaMA」を M1 搭載 Mac で実行可能に、大規模言語モデルを普通の消費者向けハードウェアで実行可能であることが示される|au Web ポータル経済・IT ニュース

掃除

- 結構 mac の容量を圧迫 7 手いるので ggml bin ファイルは削除
- 変換した gguf は残す

```sh
rm models/*.bin
ll models
```

## 次回やること

talk-llama

- [talk-llama](https://github.com/ggerganov/whisper.cpp/tree/master/examples/talk-llama)
- whisper.cpp と llama.cpp を使っている
- それ以外で使ってみるものがないか調べる
- もと：[Anyone keeping tabs on Vicuna, a new LLaMA-based model? · ggerganov/llama.cpp · Discussion #643 · GitHub](https://github.com/ggerganov/llama.cpp/discussions/643#discussioncomment-5533894)

fast-chat

- [GitHub - lm-sys/FastChat: An open platform for training, serving, and evaluating large language models. Release repo for Vicuna and Chatbot Arena.](https://github.com/lm-sys/FastChat)
- インターフェースみたいな感じ
