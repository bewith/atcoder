# About This Repos

## How to install

### Clone This Repos
```
git clone https://github.com/bewith/atcoder.git
```

### srcフォルダ以下を削除
```
rm -rf src
```

### Docker Imageの作成 & 起動
```
docker-compose up -d
```

### Dockerに接続
```
docker-compose exec atcoder bash
```

### atcodertoolsの不具合修正
```
vi /usr/local/lib/python3.9/site-packages/atcodertools/common/language.py
```

```diff
- submission_lang_pattern=re.compile(".*Python3.*|^Python$"),
+ submission_lang_pattern=re.compile(".*Python.*|^Python$"),
```

## How to use
@see https://github.com/kyuridenamida/atcoder-tools

```
docker-compose exec atcoder bash
cd /src
atcoder-tools gen abs --lang python --workspace .
cd abs/PracticeA/
atcoder-tools test
```
