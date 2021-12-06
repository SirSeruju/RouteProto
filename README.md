| Name        | Start byte        | Size in bytes  |
| ----------- | ----------------- | -------------- |
| end port    | 0                 | 2              |
| current hop | 2                 | 1              |
| IPs count   | 3                 | 1              |
| IPs         | 4                 | IPs count * 4  |
| data        | 4 + IPs count * 4 | ...            |

