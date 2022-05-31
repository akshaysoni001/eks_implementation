from app.discovery.eks_discovery import EKSClusterClient


if __name__ == "__main__":
    eks_cluster = EKSClusterClient()
    eks_cluster.get_eks_metadata()
