[![Python Versions](https://github.com/primetimetank21/hackUMBC2022/actions/workflows/python-versions.yml/badge.svg)](https://github.com/primetimetank21/hackUMBC2022/actions/workflows/python-versions.yml)

![TrustDeFi logo](https://github.com/primetimetank21/hackUMBC2022/blob/develop/images/logo.png)

*Don't let untrustworthy transactions put you in a DeFicit; TrustDeFi and we'll help you make the best of it!*

## Inspiration

Users of cryptocurrency are constantly targeted by various fraud and various threats on their holdings. Because of a lack of regulation and knowledge in the crypto space, attackers have been able to exploit protocols and users alike, resulting in over $10 billion in theft and scams in 2021 alone. Of these attacks, roughly $38 million was stolen from Alpha Homora V2, a yield farming protocol. One method of helping to protect companies and consumers, along with their assets is to instill trust in the parties with whom they are transacting with. Enter TrustDeFi.

## What it does

TrustDeFi is a tool that helps users make a better-informed decisions when interacting with other users on the Ethereum Main network. This tool does a number of things:

- lists a fair amount of transactions executed by an ETH wallet address with the associated transaction hash and date. 

- allows users to see the history of the wallet address (or smart contract) they are interacting with, including risky transactions they were possibly involved with

- displays a trustworthiness label to help determine distinguish how the address is / has been used

## How we built it

TrustDeFi was built using Python3 with matplotlib, seaborn, sklearn, pandas, os, requests, json, beautiful soup, and fast api. We web scraped data from Covalent and Etherscan to provide transaction data of the exploiters discussed then cleaned the data to remove any unnecessary data. To visualize the data, we created bar plots that highlight where the money is being sent to/from. The tool we created was built as a script in VSCode along with the Notebook created in Deepnote.

## Challenges we ran into

One of the first challenges we encountered was which direction to take this project. There was so much that we wanted to do with it. We wanted to incorporate Machine Learning and Real-Time updated data. The issue wasn't the skill / knowledge base; rather, our biggest obstacle was time!

## Accomplishments that we're proud of

We are proud that we were able to produce a working model utilizing both of the APIs we intended to develop with. Also, we are proud that we got to visualize the data of the exploiters and see where they were sending and receiving funds.

## What we learned

We learned that exploiters often have inactive wallets after a major attack. The likely reason is that they were blacklisted from the platform they were using. With TrustDeFi, consumers would have access to this information, which could be very beneficial for them (and their wallets!). Another thing we learned is that the tool we developed will get transaction data since the creation of the wallet. Another lesson from this project is understanding the interaction between the exploiter and their victims.

## What's next for TrustDeFi

Next steps include further developing the GUI for the application. We also want to implement a machine learning model that we would train to classify whether a user's wallet is trustworthy or not. More on this, we would like to introduce a spectrum of trustworthiness to provide a thorough score for each wallet that gets searched with our application. 

