from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import Elasticache, RDS
from diagrams.aws.network import ELB, Route53

with Diagram("Cluster Web Services", show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"),
                    ECS("web2"),
                    ECS("web3")]
    with Cluster("DB Cluster"):
        db_master = RDS("userdb")
        db_master = [RDS("userdb ro")]

    memcached = Elasticache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_master
    svc_group >> memcached