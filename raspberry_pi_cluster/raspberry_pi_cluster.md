# Raspberry Pi Cluster

## Hardware

- Raspberry Pi B4 RAM 4GB × 3
- クラスターケース
  - Raspberry Pi の方にケースがついてくるけど多分買う
- SDカード × 3
- スイッチングハブ
- LAN ケーブル
- USB充電器 6ポート

## Software

- OS
  - Ubuntu 22.04.1 LTS
- Kubernetes: 1.25
- cri-o: 1.25.1

## architecture

| raspberry pi | host        | role   | IP address     | MAC address       | disk  |
| ------------ | ----------- | ------ | -------------- | ----------------- | ----- |
| 4B           | k8s-master  | master | 192.168.10.101 | e4:5f:01:e2:59:e4 |       |
|              | k8s-worker1 | worker | 192.168.10.102 | e4:5f:01:e2:59:14 | 128GB |
|              | k8s-worker2 | worker | 192.168.10.103 | e4:5f:01:e2:5a:1e |       |

## OS

- [SDカードの準備 - 3枚](https://zenn.dev/ie4/articles/8e6a5ae9ac1250)

## network

| raspberry pi | role     | IP address     |
| ------------ | -------- | -------------- |
| 4B           | master   | 192.168.10.101 |
|              | worker 1 | 192.168.10.102 |
|              | worker 2 | 192.168.10.103 |
|              |          |                |

やらなくていいかも(よくわからずにやった)

`/etc/netplan/99-network.yaml`

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: false
      dhcp6: false
      addresses:
        - 192.168.1.101/24 # ラズパイ毎でIPを変更してください。（末尾がそれぞれ101, 102, 103になります。）
      routes: # 自宅のルーターからゲートウェイを調べて下さい。ここを間違えるとラズパイはネットに繋がらなくなります…
        - to: default
          via: 192.168.10.1
      nameservers:
        addresses:
          - 192.168.10.1
```

```bash
sudo netplan apply
ip a
```

ホスト名の変更

@raspberry_pi

ラズパイのOSインストール時に指定したので以下のコマンドは不要

```bash
sudo hostnamectl set-hostname <hostname>
hostname
```

DNS的な

`etc/hosts`

```hosts
192.168.1.101   k8s-master kube-master.kamoj.com
192.168.1.102   k8s-worker1 kube-master1.kamoj.com
192.168.1.103   k8s-worker2 kube-worker2.kamoj.com
```

IPv6 の無効化

`etc/sysctl.conf`の最後に追記

```conf
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.eth0.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

timezone, keymap の変更

今回は OS インストール時に設定したので不要

```bash
# タイムゾーンの変更
sudo timedatectl set-timezone Asia/Tokyo

# keymapの変更
sudo localectl set-keymap jp106
```

### Router

NEC のルーターなら以下のように固定 IP を割り当てることができる

- [DHCP固定割当設定手順](https://www.aterm.jp/support/guide/category/special/dhcp_assign/007/main.html)
- <aterm.me>
- IPv4LAN設定
  - IP address: 192.168.10.1/24
  - DHCPサーバ
    - DHCP 割当アドレス: 192.168.10.101 - 192.168.10.200
- DHCP 固定割当設定
  - DHCP 割当アドレスから選択

## ssh

## Kubernetes

- [kubeadm のインストール](https://kubernetes.io/ja/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

- before
  - OS: Ubuntu 16.04+
  - memory >= 2GB per machine
  - core >= 2 per machine
  - クラスター内のすべてのマシン間で通信可能なネットワーク
  - ユニークなhostname、MACアドレス、とproduct_uuid
  - port: private なのでOK
  - swap: off

iptablesがブリッジを通過するトラフィックを処理できるようにする

```bash
lsmod | grep br_netfilter
sudo modprobe br_netfilter
```

```bash
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system
```

swap の無効化

```bash
sudo swapoff -a
```

iptablesがnftablesバックエンドを使用しないようにする 

```bash
# レガシーバイナリがインストールされていることを確認してください
sudo apt install -y iptables arptables ebtables

# レガシーバージョンに切り替えてください。
sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
sudo update-alternatives --set arptables /usr/sbin/arptables-legacy
sudo update-alternatives --set ebtables /usr/sbin/ebtables-legacy
```

cri-o のインストール

- [CRIのインストール](https://kubernetes.io/ja/docs/setup/production-environment/container-runtimes/)

```bash
sudo modprobe overlay

# 必要なカーネルパラメータの設定をします。これらの設定値は再起動後も永続化されます。
cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF
sudo sysctl --system
```

root 化は適宜。(書き換えるのめんどくなったので)

以下の方法は、2回目以降 Hash Sum mismatch で失敗して原因がわからず、結局スクリプトを利用してインストールした。

```bash
OS=xUbuntu_22.04
VERSION=1.25
echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/ /" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
echo "deb http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$VERSION/$OS/ /" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable:cri-o:$VERSION.list

curl -L https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable:cri-o:$VERSION/$OS/Release.key | apt-key add -
curl -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/Release.key | apt-key add -

apt update
apt install -y cri-o cri-o-runc
```

スクリプトを使う場合(GitHub に書いてる)

```bash
sudo apt install -y jq
curl https://raw.githubusercontent.com/cri-o/cri-o/main/scripts/get | sudo bash
crio --version
```

```bash
sudo systemctl daemon-reload
sudo systemctl start crio
sudo systemctl enable crio
systemctl status crio
```

- なんかエラーがでるけど問題ないらしい
  - [open /var/lib/crio/clean.shutdown.supported: no such file or directory"](https://pullanswer.com/questions/open-var-lib-crio-clean-shutdown-supported-no-such-file-or-directory)

```bash
$ systemctl status crio
...
Nov 22 23:44:26 k8s-worker1 crio[2375]: time="2022-11-22 23:44:26.472736385+09:00" level=error msg="Writing clean shutdown supported file: open /var/lib/crio/clean.shutdown.supported: no such file or directory"
Nov 22 23:44:26 k8s-worker1 crio[2375]: time="2022-11-22 23:44:26.473505966+09:00" level=error msg="Failed to sync parent directory of clean shutdown file: open /var/lib/crio: no such file or directory"
```



group?



kubeadm、kubelet、kubectlのインストール

- `kubeadm`: クラスターを起動するubectl label node work02 node-role.kubernetes.io/worker=workerコマンドです。
- `kubelet`: クラスター内のすべてのマシンで実行されるコンポーネントです。 Podやコンテナの起動などを行います。
- `kubectl`: クラスターにアクセスするためのコマンドラインツールです。

```bash
sudo apt update && sudo apt install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

コントロールプレーンノードの kubelet によって使用される cgroup ドライバーの設定

CRI の場合は、`/etc/default/kubelet`

```kubelet
KUBELET_EXTRA_ARGS=--cgroup-driver=systemd
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart kubelet
```

`kubelet` は `kubeadm` で何かしらの指示があるまで再起動し続けるらしい。

> The kubelet is now restarting every few seconds, as it waits in a crashloop for kubeadm to tell it what to do.

[cgroup で memory の有効化?](https://future-architect.github.io/articles/20220908a/)

## おまじない

```bash
sudo modprobe br_netfilter
echo '1' > /proc/sys/net/ipv4/ip_forward
```

## Kuberntes Cluster の作成

コントロールプレーンの設定@master

```bash

sudo kubeadm init --apiserver-advertise-address=192.168.10.101 --pod-network-cidr=10.244.0.0/16
```

- apiserver-advertise-address
  - このオプションを利用して明示的にAPIサーバーのadvertise addressを設定します。
  - 明示的に指定しない場合はデフォルトゲートウェ 佐野なつイに関連付けられたネットワークインターフェースを使用して設定されます。
- pod-network-cidr
  - Flannelを使用する場合、こちらを指定する必要があります。
  - Flannelはノード間をつなぐネットワークに仮想的なトンネルを構成することで、クラスター内のPod同士の通信を実現しています。
    /16と広めに設定します（GitHub - flannel-io/flannel）。

初期化後、kubeadm join 192.168.1.101:6443 --token ...という出力が出たら、どこかのテキストエディタにコピーしておきます。
このコマンドはワーカーノードを追加する際に利用します。

```bash
# ホームディレクトリに.kubeディレクトリを作成
mkdir -p ~/.kube
# Kubernetesのadmin.confを.kubeディレクトリのconfigファイルへコピー
sudo cp -i /etc/kubernetes/admin.conf ~/.kube/config
# configファイルの所有者がrootになっているのでk8suserへ変更
sudo chown $(id -u):$(id -g) ~/.kube/config
# .bashrcへ環境変数の追加
echo 'KUBECONFIG=$HOME/.kube/config' >> ~/.bashrc
# コマンドの入力補完を設定
echo "source <(kubectl completion bash)" >> $HOME/.bashrc
# 変更を適用
source ~/.bashrc
```

- [Fail running on Raspberry Pi Ubuntu 21.10](https://github.com/k3s-io/k3s/issues/4234)

```bash
sudo apt install linux-modules-extra-raspi && sudo reboot
```


Flannel

```bash
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
```

```bash
kubectl get pods -n kube-flannel
```

ロードバランサーのインストール

```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml
# ...

kubectl create secret generic -n metallb-system memberlist --from-literal=secretkey="$(openssl rand -base64 128)"
```

```bash
kubectl get pod -n metallb-system
```

## ワーカーノードをクラスターにジョイン

```bash
modprobe br_netfilter
```

```bash
sudo kubeadm join 192.168.1.101:6443 --token 3u2z7v.qx81p3azvu15ftzw --discovery-token-ca-cert-hash sha256:0e731a79605ba03cfbc823e86e8b81b2fcdcf7f1887c1d2d86239ed87fff8d04
```

```bash
kubectl get nodes
```

```bash
kubectl label node k8s-worker1 node-role.kubernetes.io/worker=worker
kubectl label node k8s-worker2 node-role.kubernetes.io/worker=worker
```

```bash
ubuntu@k8s-master:~$ kubectl get nodes
NAME          STATUS   ROLES           AGE   VERSION
k8s-master    Ready    control-plane   46h   v1.26.0
k8s-worker1   Ready    <none>          14m   v1.26.0
k8s-worker2   Ready    <none>          81s   v1.26.0
```

```bash
kubectl label node k8s-worker1 node-role.kubernetes.io/worker=worker
kubectl label node k8s-worker2 node-role.kubernetes.io/worker=worker
```

```bash
ubuntu@k8s-master:~$ kubectl get nodes
NAME          STATUS   ROLES           AGE   VERSION
k8s-master    Ready    control-plane   46h   v1.26.0
k8s-worker1   Ready    worker          33m   v1.26.0
k8s-worker2   Ready    worker          19m   v1.26.0
ubuntu@k8s-master:~$ kubectl get pods --all-namespaces 
NAMESPACE        NAME                                 READY   STATUS    RESTARTS       AGE
kube-flannel     kube-flannel-ds-dm67n                1/1     Running   0              33m
kube-flannel     kube-flannel-ds-hj2zl                1/1     Running   516            45h
kube-flannel     kube-flannel-ds-kx9c8                1/1     Running   0              20m
kube-system      coredns-787d4945fb-dhmzs             1/1     Running   0              46h
kube-system      coredns-787d4945fb-zjp28             1/1     Running   0              46h
kube-system      etcd-k8s-master                      1/1     Running   1              46h
kube-system      kube-apiserver-k8s-master            1/1     Running   1              46h
kube-system      kube-controller-manager-k8s-master   1/1     Running   1              46h
kube-system      kube-proxy-5hxm7                     1/1     Running   1              46h
kube-system      kube-proxy-8dtn8                     1/1     Running   0              20m
kube-system      kube-proxy-xfrd2                     1/1     Running   0              33m
kube-system      kube-scheduler-k8s-master            1/1     Running   1              46h
metallb-system   controller-577b5bdfcc-ql2fb          1/1     Running   1 (31m ago)    4h28m
metallb-system   speaker-j5shp                        1/1     Running   0              19m
metallb-system   speaker-lfvxc                        1/1     Running   0              32m
metallb-system   speaker-ttxpb                        1/1     Running   2 (101m ago)   4h28m
ubuntu@k8s-master:~$ 
```

## サービスメッシュ

Linkerd のシェアがトップらしいので使う。

## 動作確認

<https://future-architect.github.io/articles/20220908a/>

## 可用性

<https://future-architect.github.io/articles/20220908a/>

## 再起動

<https://future-architect.github.io/articles/20220908a/>


## reset

```bash
sudo kubeadm reset && rm ~/.kube/config && rm -r /etc/cni/net.d && sudo iptables -F && sudo iptables -t nat -F && sudo iptables -t mangle -F && sudo iptables -X
sudo kubeadm init --apiserver-advertise-address=192.168.10.101 --pod-network-cidr=10.244.0.0/16
sudo cp -i /etc/kubernetes/admin.conf ~/.kube/config && sudo chown $(id -u):$(id -g) ~/.kube/config
```

## commands

```bash
kubectl get pods --all-namespaces 
```

## debug

### cri-o Hash Sum mismatch

結局これで。

```bash
sudo apt install -y jq
curl https://raw.githubusercontent.com/cri-o/cri-o/main/scripts/get | sudo bash
```

発生事象

```bash
Err:1 http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/1.25/xUbuntu_22.04  cri-o 1.25.1~1                                                                                                                                                           
  Hash Sum mismatch
  Hashes of expected file:
   - SHA256:739aed35eba19415193bc4da024f7a903d0849e1e7729a06077f77a8a4367e4f
   - SHA1:9a819763a88d511aa325e39661933c1eb9eb5d01 [weak]
   - MD5Sum:d8ff69c97bfbebe91f056062e44d34d7 [weak]
   - Filesize:20944244 [weak]
  Hashes of received file:
   - SHA256:37b1d24e5b0c249adae8c9686827b64c6cca51ee4ee37e1abc877f251809ec2f
   - SHA1:36229b1f76ca496dca1b07f322e3556a10543f09 [weak]
   - MD5Sum:7e0629a3270b41c6a0b910d242e032d1 [weak]
   - Filesize:15970304 [weak]
  Last modification reported: Tue, 15 Nov 2022 19:34:31 +0000
Fetched 16.0 MB in 11min 24s (23.4 kB/s)                                                                                                                                                                                                                                                 
E: Failed to fetch http://mirror-jp.firstyear.id.au/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/1.25/xUbuntu_22.04/arm64/cri-o_1.25.1~1_arm64.deb  Hash Sum mismatch
   Hashes of expected file:
    - SHA256:739aed35eba19415193bc4da024f7a903d0849e1e7729a06077f77a8a4367e4f
    - SHA1:9a819763a88d511aa325e39661933c1eb9eb5d01 [weak]
    - MD5Sum:d8ff69c97bfbebe91f056062e44d34d7 [weak]
    - Filesize:20944244 [weak]
   Hashes of received file:
    - SHA256:37b1d24e5b0c249adae8c9686827b64c6cca51ee4ee37e1abc877f251809ec2f
    - SHA1:36229b1f76ca496dca1b07f322e3556a10543f09 [weak]
    - MD5Sum:7e0629a3270b41c6a0b910d242e032d1 [weak]
    - Filesize:15970304 [weak]
   Last modification reported: Tue, 15 Nov 2022 19:34:31 +0000
```

調べたこと

- [About apt Hash Sum mismatch problem](https://twitter.com/mattn_jp/status/1280499700446216207)

```bash
OS=xUbuntu_22.04
VERSION=1.25
echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/ /" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
echo "deb http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$VERSION/$OS/ /" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable:cri-o:$VERSION.list

curl -L https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable:cri-o:$VERSION/$OS/Release.key | apt-key add -
curl -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/Release.key | apt-key add -

apt update
apt install -y cri-o cri-o-runc
```

```bash
curl -fsSL https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/libcontainers-archive-keyring.gpg
curl -fsSL https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$VERSION/$OS/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/libcontainers-crio-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/libcontainers-archive-keyring.gpg] https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
echo "deb [signed-by=/usr/share/keyrings/libcontainers-crio-archive-keyring.gpg] https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$VERSION/$OS/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable:cri-o:$CRIO_VERSION.list
```

### failed to set bridge addr: could not add IP address to "cni0": permission denied

- [](https://stackoverflow.com/questions/62408028/kubelet-failed-to-createpodsandbox-for-coredns-failed-to-set-bridge-addr-c)

### "Container runtime network not ready" networkReady="NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: No CNI configuration file in /etc/cni/net.d/

- ["No CNI configuration file in /etc/cni/net.d/" condition remains after CNI has been configured](https://github.com/cri-o/cri-o/issues/4276)
  - `touch /etc/cni/net.d/99-dummy.conf`

### Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox

```log
  Warning  FailedCreatePodSandBox  3s                  kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-565d847f94-8trzb_kube-system_d9e23a72-c5a0-4ea7-8b31-76c7c28fb982_0(af9215293b68f619416b82172652bed4e393b4759e808975b04bd7a54199f0b6): error adding pod kube-system_coredns-565d847f94-8trzb to CNI network "crio": plugin type="bridge" name="crio" failed (add): failed to set bridge addr: could not add IP address to "cni0": permission denied
```

- [crio on minikube: could not add IP address to "cni0": permission denied ](https://github.com/cri-o/cri-o/issues/3555)

```bash
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=0
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=0
sudo sysctl -w net.ipv6.conf.tun0.disable_ipv6=0
sudo sysctl -p
```

### Nov 28 23:54:59 k8s-master kubelet[6780]: E1128 23:54:59.364417    6780 dns.go:157] "Nameserver limits exceeded" err="Nameserver limits were exceeded, some nameservers have been omitted, the applied nameserver line is: 192.168.10.1 240b:11:2381:4400:8222:a7ff:fe94:4836 192.168.10.>

```log
Nov 28 23:54:59 k8s-master kubelet[6780]: E1128 23:54:59.364417    6780 dns.go:157] "Nameserver limits exceeded" err="Nameserver limits were exceeded, some nameservers have been omitted, the applied nameserver line is: 192.168.10.1 240b:11:2381:4400:8222:a7ff:fe94:4836 192.168.10.>
Nov 28 23:55:01 k8s-master kubelet[6780]: E1128 23:55:01.826109    6780 kubelet.go:2373] "Container runtime network not ready" networkReady="NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized"
```

### Container runtime network not ready" networkReady="NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized

kubelet





### failed to set bridge addr: could not add IP address to "cni0": permission denied



### flannel Error registering network: operation not supported

- [ Error registering network: operation not supported #1028 ](https://github.com/flannel-io/flannel/issues/1028)

### Container runtime network not ready: cni config uninitialized

- [Container runtime network not ready: cni config uninitialized](https://stackoverflow.com/questions/49112336/container-runtime-network-not-ready-cni-config-uninitialized)

### coredns Pending

- [Installing a Pod network add-on](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network)

You must deploy a Container Network Interface (CNI) based Pod network add-on so that your Pods can communicate with each other. Cluster DNS (CoreDNS) will not start up before a network is installed.

CoreDNS は CNI ベースのポッドネットワークアドオンをデプロイする必要がある

### Error registering network: operation not supported

- [Error registering network: operation not supported](https://github.com/flannel-io/flannel/issues/1028)
- [Error registering network: operation not supported #905](https://github.com/flannel-io/flannel/issues/905)
- [flannel error: Error registering network: operation not supported](https://www.reddit.com/r/kubernetes/comments/u1hzra/flannel_error_error_registering_network_operation/)

現状

```bash
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
```

## Failed to check for processor microcode upgrades.

- [Ubuntu 22.04 LTS on WSLで出るエラー対処 : Failed to retrieve available kernel versions. Failed to check for processor microcode upgrades.](https://level69.net/archives/30464)

## log

```bash
ubuntu@k8s-master:~$ sudo kubeadm init --apiserver-advertise-address=192.168.10.101 --pod-network-cidr=10.244.0.0/16                                                                                                                                                                      
[init] Using Kubernetes version: v1.25.4                                                                                                                                                                                                                                                  
[preflight] Running pre-flight checks                                                                                                                                                                                                                                                     
        [WARNING SystemVerification]: missing optional cgroups: blkio                                                                                                                                                                                                                     
[preflight] Pulling images required for setting up a Kubernetes cluster                                                                                                                                                                                                                   
[preflight] This might take a minute or two, depending on the speed of your internet connection                                                                                                                                                                                           
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'                                                                 そういうことするんですねー                                                                                                                             
[certs] Using certificateDir folder "/etc/kubernetes/pki"                                                                                                                                                                                                                                 
[certs] Generating "ca" certificate and key                                                                                                                                                                                                                                               
[certs] Generating "apiserver" certificate and key                                                                                                                                                                                                                                        
[certs] apiserver serving   Warning  FailedCreatePodSandBox  3s                  kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-565d847f94-8trzb_kube-system_d9e23a72-c5a0-4ea7-8b31-76c7c28fb982_0(af9215293b68f619416b82172652bed4e393b4759e808975b04bd7a54199f0b6): error adding pod kube-system_coredns-565d847f94-8trzb to CNI network "crio": plugin type="bridge" name="crio" failed (add): failed to set bridge addr: could not add IP address to "cni0": permission denied
cert is signed for DNS names [k8s-master kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 192.168.10.101]                                                                                          
[certs] Generating "apiserver-kubelet-client" certificate and key                                                                                                                                                                                                                         
[certs] Generating "front-proxy-ca" certificate and key                                                                                                                                                                                                                                   
[certs] Generating "front-proxy-client" certificate and key                                                                                                                                                                                                                               
[certs] Generating "etcd/ca" certificate and key                                                                                                                                                                                                                                          
[certs] Generating "etcd/server" certificate and key                                                                                                                                                                                                                                      
[certs] etcd/server serving cert is signed for DNS names [k8s-master localhost] and IPs [192.168.10.101 127.0.0.1 ::1]                                                                                                                                                                    
[certs] Generating "etcd/peer" certificate and key                                                                                                                                                                                                                                        
[certs] etcd/peer serving cert is signed for DNS names [k8s-master localhost] and IPs [192.168.10.101 127.0.0.1 ::1]                                                                                                                                                                      
[certs] Generating "etcd/healthcheck-client" certificate and key                                                                                                                                                                                                                          
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Starting the kubelet
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[apiclient] All control plane components are healthy after 19.711357 seconds
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config" in namespace kube-system with the configuration for the kubelets in the cluster
[upload-certs] Skipping phase. Please see --upload-certs
[mark-control-plane] Marking the node k8s-master as control-plane by adding the labels: [node-role.kubernetes.io/control-plane node.kubernetes.io/exclude-from-external-load-balancers]
[mark-control-plane] Marking the node k8s-master as control-plane by adding the taints [node-role.kubernetes.io/control-plane:NoSchedule]
[bootstrap-token] Using token: 1wt84l.e035uwia5h6ffnsr
[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
[bootstrap-token] Configured RBAC rules to allow Node Bootstrap tokens to get nodes
[bootstrap-token] Configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] Configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] Configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstrap-token] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
[kubelet-finalize] Updating "/etc/kubernetes/kubelet.conf" to point to a rotatable kubelet client certificate and key
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.10.101:6443 --token 1wt84l.e035uwia5h6ffnsr \
        --discovery-token-ca-cert-hash sha256:c8d75ebbdb5ebc5d1a8cbdac5c3bcb48ce4c818b1a049d31a013c52a4bead141 
```

kubeadm join 192.168.10.101:6443 --token vs8ys2.0biyjxmox7oqzr6m \
        --discovery-token-ca-cert-hash sha256:c74b3b9dcf2701a563d654aa911b7c64d84994c2dc327048de675defd4ba92a9 

```conf
{
    "cniVersion": "0.3.1",
    "name": "crio",
    "type": "bridge",
    "bridge": "cni0",
    "isGateway": true,
    "ipMasq": true,
    "hairpinMode": true,
    "ipam": {
        "type": "host-local",
        "routes": [
            { "dst": "0.0.0.0/0" },
            { "dst": "1100:200::1/24" }
        ],
        "ranges": [
            [{ "subnet": "10.244.0.0/16" }],
            [{ "subnet": "1100:200::/24" }]
        ]
    }
}
```

## Remark

## あとで

- Flannel
- MetalLB
