from .taiwan_twse import TaiwanTWSEDataSource

# 統一的資料源註冊表（之後可再擴充 tpex、finmind 等）
datasource_registry = {
    "taiwan_twse": TaiwanTWSEDataSource,
}
