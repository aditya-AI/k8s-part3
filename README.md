# Kubernetes - III: EKS, ALB, Auto Scaling


## EKS 
```bash
brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
```

## Node Viewer
```bash
brew tap aws/tap
brew install eks-node-viewer
```
aws sts get-caller-identity --query "Account" --output text
103877285477

eksctl create iamserviceaccount \
--cluster=basic-cluster \
--namespace=kube-system \
--name=aws-load-balancer-controller \
--attach-policy-arn=arn:aws:iam::103877285477:policy/AWSLoadBalancerControllerIAMPolicy \
--override-existing-serviceaccounts \
--region ap-south-1 \
--approve


helm repo add eks https://aws.github.io/eks-charts
helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=basic-cluster --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller

cd fastapi-helm/
helm install gpt2-eks . --values values.yaml

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard

kubectl apply -f eks-admin.yaml

kubectl -n kubernetes-dashboard create token admin-user
kubectl port-forward svc/kubernetes-dashboard -n kubernetes-dashboard 6443:443


aws iam create-policy --policy-name AWSClusterAutoScalerIAMPolicy --policy-document file://cas-iam-policy.json

eksctl create iamserviceaccount \
--cluster=basic-cluster \
--namespace=kube-system \
--name=cluster-autoscaler \
--attach-policy-arn=arn:aws:iam::103877285477:policy/AWSClusterAutoScalerIAMPolicy \
--override-existing-serviceaccounts \
--region ap-south-1 \
--approve

kubectl -n kube-system describe sa cluster-autoscaler

curl -o cluster-autoscaler-autodiscover.yaml https://raw.githubusercontent.com/kubernetes/autoscaler/master/cluster-autoscaler/cloudprovider/aws/examples/cluster-autoscaler-autodiscover.yaml