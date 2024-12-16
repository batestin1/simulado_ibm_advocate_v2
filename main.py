import streamlit as st

# Inicializa o estado das perguntas e pontuação
if "perguntas" not in st.session_state:
    st.session_state.perguntas = [
        {
            "pergunta": "What is cloud computing?",
            "alternativas": [
                "a) A marketing term invented by Amazon Web",
                "b) Salesforce applications hosted in a remote data center",
                "c) On-demand network access to shared resources",
                "d) A hardware server divided into multiple virtual servers"
            ],
            "resposta": "c"
        },
        {
            "pergunta": "How does IBM Cloud monitor the events around the lifecycle of keys as it pertains to encryption?",
            "alternativas": [
                "a) Activity Tracker",
                "b) Compliance Center",
                "c) Log Analysis",
                "d) Cloud Monitor"
            ],
            "resposta": "a"
        },
                {
            "pergunta": "What is an open source, server-based tool that builds and tests software continuously, supporting the practices of continuous integration and continuous delivery?",
            "alternativas": [
                "a) Event Streams",
                "b) MQ",
                "c) API Connect",
                "d) Jenkins"
            ],
            "resposta": "d"
        },
                {
            "pergunta": "What is an API management tool that sits between a client and a collection of backend services that enforces runtime policies to secure and control API traffic?",
            "alternativas": [
                "a) Application binaries",
                "b) Developer toolkit",
                "c) Interface component",
                "d) API Gateway"
            ],
            "resposta": "d"
        },
                {
            "pergunta": "Which IBM Cloud VMware solution is a hosted private cloud that delivers the VMware vSphere and includes the automatic deployment and configuration of an easy-to-manage logical edge firewall?",
            "alternativas": [
                "a) vCenter Server",
                "b) VMware Shared",
                "c) VMware Regulated",
                "d) VMware vSphere"
            ],
            "resposta": "a"
        },
                {
            "pergunta": "In IBM Cloud locations, what is the correct order of hierarchy",
            "alternativas": [
                "a) Geography, Country, Zone, Metro",
                "b) Geography, Metro, Country, Zone",
                "c) Geography, Country, Metro, Zone",
                "d) Country, Geography, Metro, Zone"
            ],
            "resposta": "c"
        },
                {
            "pergunta": "What must be configured after an instance of IBM Cloud Monitoring is provisioned?",
            "alternativas": [
                "a) A monitoring agent for each host that you want to monitor",
                "b) A server agent for each host that you want to monitor",
                "c) A latency agent for each host that you want to monitor",
                "d) A hosting agent for each host that you want to monitorr"
            ],
            "resposta": "a"
        },
                {
            "pergunta": "Which company introduced virtualization?",
            "alternativas": [
                "a) IBM",
                "b) Microsoft",
                "c) Compaq",
                "d) Amazon"
            ],
            "resposta": "a"
        },
                {
            "pergunta": "VSIs are deployed within a VPC on IBM CLOUD. What does VSI stand for?",
            "alternativas": [
                "a) Visible Server Instance",
                "b) Virtual Server Incident",
                "c) Virtual Service Incident",
                "d) Virtual Server Instance"
            ],
            "resposta": "d"
        },
                {
            "pergunta": "What is the function of IBM Cloud Code Engine?",
            "alternativas": [
                "a) Runs containerized workloads on a full managed, serverless platform",
                "b) Delivers complete virtual desktop envronments to users",
                "c) Allows an Enterprise to establish its own private cloud like Computing environment",
                "d) Expands the reaches of IBM Cloud infrastructures outside of IBM cloud data center"
            ],
            "resposta": "a"
        },
                {
            "pergunta": "Which practice allows IBM CLOUD to provide layered security controls across network and infrastructure?",
            "alternativas": [
                "a) Secure engineering",
                "b) Incident Management",
                "c) Data governance",
                "d) Operacional insights"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "What is Red Hat OpenShift?",
            "alternativas": [
                "a) A virtual desktop environments to users",
                "b) A software platform for building containers",
                "c) A portable, extensible, proprietary platform for managing containerized workloads and services",
                "d) An Enterprise-grade container management platform"
            ],
            "resposta": "d"
        },
                {
            "pergunta": "IBM Cloud Security and Compliance Center can help a client understand its security posture by continuously monitoring the client's_______.",
            "alternativas": [
                "a) Encryption methods",
                "b) environment",
                "c) Configurations",
                "d) Applications"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "Define data centers.",
            "alternativas": [
                "a) Centers built in multi-zone regions",
                "b) Large warehouses containing pods and racks or standardized containers of computing resourcers",
                "c) Centers that provide isolation from multizone regions in a location",
                "d) One or more buildings within a 5-mile radius in a metro region"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "List three types of cloud deployment models",
            "alternativas": [
                "a) Public, private, hybrid",
                "b) Network, public, private",
                "c) Public, server, private",
                "d) Public, private, application"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "MongoDB in an example of a(n) ________. A production instance of MongoDB is an example of a resource",
            "alternativas": [
                "a) Service",
                "b) User",
                "c) Resource group",
                "d) Access group"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "How does virtualization assist with cloud computing?"
            "alternativas": [
                "a) Speeds up mathematical calculations",
                "b) Facilitates the management of keys",
                "c) Slower provisioning",
                "d) Efficient use of physical computer hardware"
            ],
            "resposta": "d"
        },

                {
            "pergunta": "Which type of storage is best for perfomance intensive workloads?",
            "alternativas": [
                "a) File",
                "b) SAN",
                "c) Block",
                "d) Object"
            ],
            "resposta": "c"
        },

                {
            "pergunta": "Which two types of resources are always the client's responsibility in the IBM Cloud shared responsibility model?",
            "alternativas": [
                "a) Data, Applications",
                "b) Applications, Storage",
                "c) Data, Storage",
                "d) Storage, Encryption"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "Watson Knowledge Catalog is an AI lifecycle management tool used to ____________",
            "alternativas": [
                "a) Extract metadata from text",
                "b) Discover, curate, categorize, and share data asssets and models with asset control",
                "c) Deploy machine learning models across any cloud",
                "d) Measure and manage AI models in production to promote trust and confidence"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "On-demand self-service, broad network access, resource pooling, rapid elasticity, and measured services are considered which of the following?",
            "alternativas": [
                "a) The characteristics of a service provider according to IBV",
                "b) The characteristics of compute options according to Gartner",
                "c) The characteristics of deployments models according to ITG",
                "d) The characteristics of the cloud computing according to NIST"
            ],
            "resposta": "d"
        },

                {
            "pergunta": "Lower IT costs, flexible, efficient, secure, and faster time to market are all benefits of cloud _______.",
            "alternativas": [
                "a) clustering",
                "b) computing",
                "c) perfomance",
                "d) sharing"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "Which of the following are three common types of cloud storage services in IBM Cloud?",
            "alternativas": [
                "a) File, block, SSD",
                "b) Object, File, Block",
                "c) Object, SSD, SATA",
                "d) Shared, Dedicated, Private"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "Users can take advantage of cloud computing by using the __________ that the cloud provides to react more quickly to changing business needs.",
            "alternativas": [
                "a) monitoring",
                "b) Artificial Intelligence",
                "c) Agility",
                "d) Security"
            ],
            "resposta": "c"
        },

                {
            "pergunta": "When thinking about migrating workloads to IBM Cloud, what is a common key driver?",
            "alternativas": [
                "a) Agility",
                "b) DevOps",
                "c) Latency",
                "d) Security"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "What are resource efficiency, easier management, minimal downtime, and faster provisioning?",
            "alternativas": [
                "a) Visualization",
                "b) Resource Management",
                "c) Virtualization",
                "d) Dematerizalization"
            ],
            "resposta": "c"
        },

                {
            "pergunta": "What is the default support plan for anyone with a paid account on IBM CLOUD that allows for the creation of support cases or tickets?",
            "alternativas": [
                "a) Free",
                "b) Entry",
                "c) Standard",
                "d) Basic"
            ],
            "resposta": "d"
        },

                {
            "pergunta": "For industry standard regulations, such as Payment Card Industry (PCI) or Service Organization Control (SOC), how does IBM Cloud it meets the regulations?",
            "alternativas": [
                "a) Compliance reports",
                "b) Security risk manager",
                "c) Environmental assests",
                "d) Cloud Pak"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "Which type of storage is best for unstructered data that can be archived and does not need to be accessed frequentrly?",
            "alternativas": [
                "a) file",
                "b) SAN",
                "c) Block",
                "d) Object"
            ],
            "resposta": "d"
        },

                {
            "pergunta": "A customer has deployed a multi-zone IBM Cloud database. What happens if there is a networking failure in one zone of a multi-zone region, such as in case of a natural disaster?",
            "alternativas": [
                "a) Traffic is automatically redirected to a failover zone",
                "b) Load balancers wait for the network connectivity to resume",
                "c) Traffic is automatically redirected to the nearest available Cloud region",
                "d) Trafic is automatically redirected to a different service instance in the same zone"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "What is a type of application virtualization",
            "alternativas": [
                "a) Virtual Desktop",
                "b) Software-defined networking (SDN) virtualizaion",
                "c) CPU virtualization",
                "d) Local application virtualization"
            ],
            "resposta": "d"
        },

                {
            "pergunta": "Which IBM Cloud support plan allows a user to assign case severity and provides 24/7 access to the IBM cloud techinal support tea through cases, phone, and chat?",
            "alternativas": [
                "a) Free",
                "b) Basic",
                "c) Advanced",
                "d) Premium"
            ],
            "resposta": "c"
        },

                {
            "pergunta": "Which of the following are the four storage tiers associated with cloud object storage?",
            "alternativas": [
                "a) Cold tier, cool tier, warm tie, and hot tier",
                "b) Standart, glacier, deep glacier, and deep glacier archive",
                "c) Frequent access, very frequent access, infrequent access, and very infrequent access",
                "d) Smart tier, standard, vault, and cold vault"
            ],
            "resposta": "d"
        },

                {
            "pergunta": "Whatis featured in IBM Cloud Hyper Protect Crypto Services and is a dedicated key management and hardware security module (HSM)?",
            "alternativas": [
                "a) BYOK (BRING YOUR OWN KEY)",
                "b) RYOK (RENT YOUR OWN KEY)",
                "c) KYOK (KEEP YOUR OWN KEY)",
                "d) CYOK (CREATE YOUR OWN KEY)"
            ],
            "resposta": "c"
        },

                {
            "pergunta": "What is a private cloud on a shared infrastructure, which is owned and managed by a cloud service provider called?",
            "alternativas": [
                "a) Virtual Private Cloud",
                "b) private cloud",
                "c) Managed Virtual Cloud",
                "d) Dedicated Cloud"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "What is a primary benefit for companies who are considering adopting a cloud computing model?",
            "alternativas": [
                "a) Latency",
                "b) Efficiency",
                "c) Integration",
                "d) stability"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "In the IBM Cloud Console what menu option would you need to access to inspect past invoices?",
            "alternativas": [
                "a) Docs",
                "b) Manage",
                "c) Support",
                "d) Catalog"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "What is Kubernetes?",
            "alternativas": [
                "a) Identity and access management software",
                "b) Monitoring and alerting software",
                "c) Open-Source container orchestration software",
                "d) Disaster recovery software"
            ],
            "resposta": "c"
        },

                {
            "pergunta": "Which of these four concepts in IAM is an instance of provision service offering from the catalog?",
            "alternativas": [
                "a) users",
                "b) Resources",
                "c) Resource Groups",
                "d) Access groups"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "Container portability is enabled by a container carrying all of its ___________.",
            "alternativas": [
                "a) notifications",
                "b) dependencies",
                "c) rules",
                "d) proprietary workloads"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "Which option in the IBM CLOUD Console list over 200 products and services that users can choose to implement in web or mobile applications?",
            "alternativas": [
                "a) Catalog",
                "b) Docs",
                "c) Manage",
                "d) Cost Estimator"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "Which type of storage is best for organizing data in a hierarchical folder structure, and when file shares are requesteds, high perfomance is not required?",
            "alternativas": [
                "a) Object",
                "b) File",
                "c) Local",
                "d) Block"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "Which support plan in IBM Cloud includes a Technical Account Manager?",
            "alternativas": [
                "a) Free",
                "b) Basic",
                "c) Advanced",
                "d) premium"
            ],
            "resposta": "d"
        },

                {
            "pergunta": "Which role in identity and access management would enable a user to manage resources?",
            "alternativas": [
                "a) Administrator",
                "b) Editor",
                "c) Viewer",
                "d) Assistant"
            ],
            "resposta": "a"
        },

                {
            "pergunta": "By using __________ scanning, IBM Cloud ensures security readiness by adhering to security policies.",
            "alternativas": [
                "a) RBAC",
                "b) Source Code",
                "c) Encryption enforcement",
                "d) Application authentication"
            ],
            "resposta": "b"
        },

                {
            "pergunta": "How is IBM cloud being environentally conscious regaring its servers that are in service?",
            "alternativas": [
                "a) IBM Cloud is leveraging the industry's highest levels of energy efficiency encryption certification",
                "b) IBM cloud provides power efficiency and recycling in data centers",
                "c) IBM cloud incorporates security features that protect cluster infrastructure",
                "d) IBM cloud enables continuous security, compliance, and resiliency to reduce compliance costs."
            ],
            "resposta": "b"
        },

                {
            "pergunta": "When considering risk, what should banks keep in mind when adopting a cloud computing strategy?",
            "alternativas": [
                "a) Market Trends",
                "b) Competitors",
                "c) Integration",
                "d) Regulatory and Compliance Standards"
            ],
            "resposta": "d"
        },

        {
            "pergunta": "Cloud providers have redundancy built into their networks, data backup, and disaster _______",
            "alternativas": [
                "a) Storage",
                "b) Recovery",
                "c) Resiliency",
                "d) System"
            ],
            "resposta": "b"
        }
    ]
if "resultados" not in st.session_state:
    st.session_state.resultados = []

# Define a página
pagina = st.sidebar.selectbox("Escolha uma opção", ["Cadastrar Perguntas", "Responder Simulado"])

if pagina == "Cadastrar Perguntas":
    st.title("Cadastro de Perguntas")

    with st.form("cadastro"):
        pergunta = st.text_input("Digite a pergunta:")
        alternativa_a = st.text_input("Alternativa a)")
        alternativa_b = st.text_input("Alternativa b)")
        alternativa_c = st.text_input("Alternativa c)")
        alternativa_d = st.text_input("Alternativa d)")
        resposta = st.selectbox("Qual é a resposta correta?", ["a", "b", "c", "d"])
        enviar = st.form_submit_button("Cadastrar Pergunta")
        
        if enviar:
            st.session_state.perguntas.append({
                "pergunta": pergunta,
                "alternativas": [
                    f"a) {alternativa_a}",
                    f"b) {alternativa_b}",
                    f"c) {alternativa_c}",
                    f"d) {alternativa_d}"
                ],
                "resposta": resposta
            })
            st.success("Pergunta cadastrada com sucesso!")

elif pagina == "Responder Simulado":
    st.title("Simulado IBM Cloud Advocate v2")

    with st.form("simulado"):
        respostas = []
        for idx, pergunta in enumerate(st.session_state.perguntas):
            st.write(f"**{idx + 1}. {pergunta['pergunta']}**")
            resposta = st.radio(
                f"Escolha uma alternativa para a pergunta {idx + 1}:",
                pergunta["alternativas"],
                key=f"resposta_{idx}"
            )
            respostas.append(resposta)

        enviar = st.form_submit_button("Finalizar Simulado")

        if enviar:
            # Verifica respostas e calcula a pontuação
            acertos = 0
            total = len(st.session_state.perguntas)
            resultados = []
            
            for idx, resposta in enumerate(respostas):
                correta = st.session_state.perguntas[idx]["alternativas"][
                    ord(st.session_state.perguntas[idx]["resposta"]) - ord("a")
                ]
                if resposta == correta:
                    acertos += 1
                    resultados.append((idx + 1, True, correta))
                else:
                    resultados.append((idx + 1, False, correta))

            st.session_state.resultados = resultados
            st.write("### Resultado Final")
            st.write(f"Você acertou **{acertos} de {total}** perguntas.")
            media = (acertos / total) * 100
            st.write(f"**Média de Acertos:** {media:.2f}%")

            if media >= 60:
                st.success("Parabéns! Você está pronto para fazer a prova!")
            else:
                st.error("Você não atingiu 60% de acertos. Tente novamente.")

            # Mostra os detalhes de cada pergunta
            st.write("### Resumo das Respostas")
            for idx, (num, acertou, correta) in enumerate(st.session_state.resultados):
                if acertou:
                    st.write(f"**Pergunta {num}:** ✅ Resposta correta.")
                else:
                    st.write(f"**Pergunta {num}:** ❌ Resposta incorreta. Resposta correta: {correta}")
