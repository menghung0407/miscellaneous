# ACID

----

## About

- 是 Transaction 的特性
- 1983 年 被提出
- Atomicity 原子性、Consistency 一致性、Isolation 隔離性、Durability 持久性

----

## 什麼是 Transaction ?

- 中文翻作 "交易" or "事務"
- 是資料庫執行過程中的一個 "邏輯單位" (unit of work)
- 一個 transaction 中可以包含多個對資料庫操作的行為
- 兩種結局: 全部執行成功 或 全部不執行
    - 全部執行成功: commit
    - 只要有任一個 SQL 失敗: rollback
- 主要解決問題: 需要一起發生的事件但事件或事件的參與者不同時或不一致的問題

----

### Atomicity 原子性

- 將整個 transaction 視為一個不可分割的邏輯單位
- 成功 or 失敗，沒有成功一半
- 任一操作沒有完成，就會回到初始狀態

----

### Consistency 一致性

- 在 transaction 開始之前和結束以後，資料庫的完整性沒有被破壞
- 例子:
    - 1.雙方的錢都不能小於 0
    - 2.雙方錢的總和不能改變
- 仰賴應用系統來定義

----

### Isolation 隔離性

- transaction 過程中，不會被其他 transaction 干擾
- 例子:
    - A 有 500$，給 B 100$， 給 C 100$，同時發生交易時... A 最後剩餘的 $$ 為 400$ (A
      嘴角上揚....)
- 常見的 3 種錯誤
    - Dirty Read
        - 讀到其他 transaction 未完成的資料
    - Non-repeatable read
        - 同樣的對象，回傳的結果不同
    - Phantom Read
        - 結果集不同
- 常見的 4 種隔離機制
    - Read Uncommitted
    - Read Committed
    - Repeatable Read
    - serializable

----

### Durability 持久性

- 保證一但 transaction 成功資料就會被保留 (硬碟)

----

#### Transaction 併發的幾種錯誤

- Dirty Read
    - 一個 transaction 在處理過程中讀取了另外一個 transaction 未提交的數據
    - 例如: 計算月薪時...
- Non-repeatable read
    - 在同一個 transaction 當中，同樣的對象有不同的回傳結果
- Phantom Read
    - 在 Repeatable Read 隔離級別下
    - ![](D:\github\misc\miscellaneous\static\acid\phantom_read.png)

----

#### Isolation 相關的幾種隔離機制

- Read Uncommitted
- Read Committed
- Repeatable Read
- serializable isolation 序列化隔離
    - 序列化隔離的實現方法有 3 種：
        1. 字面上的，連續 (serially) 執行 transactions。
        2. 二階段鎖 (Two-Phase Locking 2PL)，主宰數十年的實作方式。
        3. 優化並發控制技術，就像有了序列化能力的快照隔離。

----

- 髒讀 Dirty Read
- 不可重複讀 Non-repeatable read
- 幻讀 Phantom Read

#### 競爭條件 (race condition)

- dirty writes
- lost update 更新遺失
- write skew
- phantoms

##### 計數器的例子

- 2 個 user
- 同樣的動作: 1.取得計數器 2.增加計數器
- 圖片示例:
- ![](D:\github\misc\miscellaneous\static\acid\figure_7-1.png)

----

- 死結 (deadlock)

----

- Two-Phase Locking 二階段鎖
- Serializable Snapshot Isolation 序列化快照隔離