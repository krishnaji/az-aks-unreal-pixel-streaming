FROM --platform=${BUILDPLATFORM:-linux/amd64} node:lts-alpine
ENV NODE_ENV=production
WORKDIR /usr/src/app
COPY . .
RUN npm install --production --silent  
RUN chown -R node /usr/src/app

ENTRYPOINT ["node", "matchmaker.js"]