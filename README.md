# Local Deep Researcher

This is a **fully local, privacy-preserving AI research agent** that uses [Microsoft AutoGen](https://github.com/microsoft/autogen) and a locally hosted LLM via [Ollama](https://ollama.com/) to perform iterative web research, completely offline from SaaS APIs.

> **Note**: This is a toy example, intended for demonstration and experimentation purposes.

---

## Features

- **Web search loop** using DuckDuckGo (no API key needed)
- **Conversational agents** (AutoGen) that:
  - Generate search queries
  - Summarize search results
  - Reflect on missing information
  - Refine queries to dig deeper
-  **LLM-powered** with any model from Ollama (`llama3.2`, `mistral`, etc.)
-  100% local – **no OpenAI / cloud API required**
-  Powered by [AutoGen](https://github.com/microsoft/autogen)

## How to Run the Script
- Start Ollama (in another terminal):
```bash
ollama pull llama3.2
ollama serve
```

- Run the research script:
```bash
 python research.py "How does climate change influence food security?"
```

## Example Output 

```markdown

 Loop 1 | Query: How does climate change influence food security?

>>>>>>>> USING AUTO REPLY...

>>>>>>>> USING AUTO REPLY...

>>>>>>>> USING AUTO REPLY...

 Loop 2 | Query: "what are climate change impacts on agriculture globally"

>>>>>>>> USING AUTO REPLY...

>>>>>>>> USING AUTO REPLY...

>>>>>>>> USING AUTO REPLY...
# Research Summary

**Climate Change and Food Security: A Complex and Interconnected Relationship**
====================================================

### Introduction

Climate change is a growing concern that affects agriculture and food security in complex and interdependent ways. While the relationship between climate change and food security is not fully understood, research suggests that climate change can have significant impacts on global food availability, access, utilization, and stability.

### Impact of Climate Change on Food Security
--------------------------------------

*   According to Forbes and Fifth ([1](https://forbes5.pitt.edu/article/climate-change-effects-food-security)), the current evidence on climate change's impact on agriculture is limited, and most available research only considers average effects and variations, not extreme events.
*   The World Bank Group reports that the number of people suffering acute food insecurity increased from 135 million in 2019 to 345 million in 82 countries by June 2022 ([2](https://www.worldbank.org/en/news/feature/2022/10/17/what-you-need-to-know-about-food-security-and-climate-change)).
*   Climate change can lead to production disruptions, local availability limitations, and price increases, as noted by the USDA ([3](https://www.usda.gov/about-usda/general-information/priorities/climate-solutions/climate-change-global-food-security-and-us-food-system)).

### Impact of Climate Change on Nutritional Content
------------------------------------------------

*   Research suggests that climate change can affect human nutrition and health indicators, particularly if atmospheric CO2 concentrations increase ([4](https://www.frontiersin.org/journals/climate/articles/10.3389/fclim.2022.941842/full)).

### McMichael, A. J., Manson-Caulfield, T., & Evans, T. G. (2007). Food security after climate change. Climatic Change, 96(1-2), 57–71.

### O'Brien, M., Eakin, C. E., & Wiebe, K. L. (2014). Climate change and adaptation in agriculture: Opportunities and constraints, policy options and next steps for an uncertain future. Environment Department South Asia.

### Parker, D., Teller, A., & Williams, R. J. (2009). Predicting the relative impact of global warming vs. land use change on crop yields in Africa in 2050. Agricultural Systems, 100(1-3), 121–132.

### Rosenzweig, C., Smith, P., & Mason-D'Almeida, R. E. (2007). Preparing for food insecurity in a changing climate. Climate and Development Knowledge Network.

## Topic
How does climate change influence food security?




```

---

## ️ Requirements

- Python 3.10+
- [`ollama`](https://ollama.com/download) (run `ollama serve`)
- Python packages:
  ```bash
  pip install -r requirements.txt


## Ideal For
- Tinkering with AutoGen in a local environment

- Exploring agent-based research flows

- Building privacy-first research agents