// #include <cstdint>
// #include <cstddef>
// #include <cstddef>
// #include "types.h"

// struct PageTableEntry {
//     uint64_t pfn          : 40;  // 物理页框号（40位）
//     uint64_t present      : 1;   // 存在位
//     uint64_t writable     : 1;   // 可写位
//     uint64_t user_accessible : 1; // 用户可访问位
//     uint64_t accessed     : 1;   // 访问位
//     uint64_t dirty        : 1;   // 修改位
//     uint64_t cache_disable: 1;   // 禁用缓存位
//     uint64_t reserved     : 18;  // 保留位（用于扩展）
// };

// struct PageTable {
//     PageTableEntry entries[512];  // 每页512个表项（x86架构）
//     phys_addr_t base_addr;        // 页表物理基址
//     int level;                    // 页表级别（0=最底层）
//     refcount_t ref_count;         // 引用计数
// };

