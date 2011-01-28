Sphinx S6 サンプル
===================


このスライドについて
----------------------
このプレゼンテーションは

* S6 (c) 2007 Cybozu Labs, Inc.
* Sphinx
* S6 Sphinxテーマ

で作成した、Sphinx S6テーマ利用サンプルです。

インストール方法
------------------

インストール

.. code-block:: bash

    $ easy_install sphinxcontrib-theme-s6

conf.py 設定

.. code-block:: python

    extensions = ['sphinxcontrib.theme.s6']
    html_theme = 's6'


スライド表示の例
-------------------

* 箇条書き
    1. 番号付き箇条書き
    2. http://sphinx-users.jp/

* **強調** , *エモーション*
* `リテラル` , ``リテラル``
* :command:`command`


スライド切替エフェクト
-----------------------
種類

* スライド: 横にslide
* フェード: fade
* フェード2: fadeScale
* 上からフェード: fadeScaleFromUp
* 拡大: fadeScaleFromUpTransparent


エフェクト : スライド
----------------------
右から左にスライドインします

::

    .. raw:: html
        <script>s6.page({effect: 'slide'});</script>

.. raw:: html

    <script>s6.page({effect: 'slide'});</script>


エフェクト : フェード
----------------------
フェードイン・フェードアウトで切り替えます（デフォルト動作）

::

    .. raw:: html
        <script>s6.page({effect: 'fade'});</script>

.. raw:: html

    <script>s6.page({effect: 'fade'});</script>


エフェクト : 縮小フェードアウト
--------------------------------
現在のスライドを縮小アニメーションして次のスライドに切り替えます

::

    .. raw:: html
        <script>s6.page({effect: 'fadeScale'});</script>

.. raw:: html

    <script>s6.page({effect: 'fadeScale'});</script>


エフェクト : 縮小フェードイン
------------------------------
次のスライドを縮小アニメーションしながら表示します

::

    .. raw:: html
        <script>s6.page({effect: 'fadeScaleFromUp'});</script>

.. raw:: html

    <script>s6.page({effect: 'fadeScaleFromUp'});</script>


拡大エフェクト
---------------
次のスライドを **半透明** 縮小アニメーションしながら表示します

::

    .. raw:: html
        <script>s6.page({effect: 'fadeScaleFromUpTransparent'});</script>

.. raw:: html

    <script>s6.page({effect: 'fadeScaleFromUpTransparent'});</script>


アクション
------------
スライド内でエレメントを動かすアクションの種類

* fade: fade in
* move: 移動
* scale: 拡大縮小


アクション : フェードイン
--------------------------
対象のエレメントを複数回に分けてフェードイン表示します。

* 箇条書きの文章１
* 箇条書きの文章２
* 箇条書きの文章３


.. raw:: html

    <script>
    s6.page({
        styles: {
            'ul/li': {display:'none'},
        },
        actions: [
            ['ul/li[0]', 'fade in', '0.3'],
            ['ul/li[1]', 'fade in', '0.3'],
            ['ul/li[2]', 'fade in', '0.3']
        ]
    });
    </script>


アクション : 移動
-------------------
対象のエレメントを移動させながら表示したり非表示にしたりします。

* 箇条書きの文章１
* 箇条書きの文章２
* 箇条書きの文章３


.. raw:: html

    <script>
    s6.page({
        actions: [
            ['ul', 'move', '5.0', [0,0],[100,0]],
        ]
    });
    </script>


センタリング
-------------

.. raw:: html

    <script>
    s6.page({
        styles: {
            h2: {fontSize:'150%',textAlign:'center',margin:'30% auto'}
        }
    });
    </script>


画像をレイアウトする例
-----------------------
* コミュニティー:
   * Python, Sphinx
* 言語:
   * Python, reStructuredText

.. figure:: sphinxusers.jpg

.. raw:: html

    <script>
    s6.page({
        styles: {
            'div': {textAlign: 'right'},
            'div/img': {width: '60%', opacity: 0.9}
        }
    });
    </script>


Textと画像のレイアウト例
--------------------------

.. code-block:: rst

    Sphinxのサンプル
    =================

    Sphinxとは何か？
    -----------------
    * ドキュメント生成のツール
    * reStructuredText記法(Wikiっぽい?
    * ページ間のリンクを自動生成
    * 強力なコードハイライト
    * HTML, PDF, ePub, htmlhelp, latex, man...

.. figure:: sphinx-sample.jpg

.. raw:: html

    <script>
    s6.page({
        styles: {
            'div[0]': {width: '60%', position:'absolute', left:'0', marginTop:'0.3em'},
            'div[0]/div/pre': {fontSize:'35%', padding:'1em'},
            'div[1]': {position:'absolute', right:'0', bottom: '0', width:'60%'}
        }
    });
    </script>

