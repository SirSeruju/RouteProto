class ProtoMeta:
    def get(self, connection):
        self.port = int.from_bytes(connection.recv(2), 'big')
        self.current_hop = int(connection.recv(1)[0])
        ips_count = int(connection.recv(1)[0])
        ips = []
        for i in range(ips_count):
            ips.append(connection.recv(4))
        self.ips = ips
        self.data = b""
        BLOCK_SIZE = 65536
        while True:
            data = connection.recv(BLOCK_SIZE)
            self.data += data
            if len(data) != BLOCK_SIZE:
                break

    def getNextProtoMeta(self):
        data = b""
        data += self.port.to_bytes(2, "big")
        data += (self.current_hop + 1).to_bytes(1, "big")
        data += len(self.ips).to_bytes(1, "big")
        for ip in self.ips:
            data += ip
        data += self.data
        return data

    def isLast(self):
        return self.current_hop + 1 == len(self.ips)

    def getData(self):
        return self.data

    def __str__(self):
        def formatIP(ip):
            ip = list(ip)
            ip = ".".join(list(map(str, ip)))
            return ip

        def formatIPs(ips, port, current_hop):
            sIPs = []
            for i, ip in enumerate(ips):
                ip = formatIP(ip)
                if i + 1 == len(ips):
                    ip = ip + ":" + str(port)
                if i == current_hop:
                    ip = "|" + ip + "|"
                sIPs.append(ip)
            return " -> ".join(sIPs)

        return formatIPs(self.ips, self.port, self.current_hop)
