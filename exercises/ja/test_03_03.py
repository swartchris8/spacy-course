def test():
    assert nlp.meta["name"] == "core_web_sm", "正しいモデルをロードしましたか？"
    assert "print(nlp.pipe_names)" in __solution__, "パイプラインの名前をプリントしましたか？"
    assert "print(nlp.pipeline)" in __solution__, "パイプラインをプリントしましたか？"

    __msg__.good(
        "Well done！今あるパイプラインについて調べたくなったときは、nlp.pipe_namesやnlp.pipelineを使ってプリントしましょう。"
    )
