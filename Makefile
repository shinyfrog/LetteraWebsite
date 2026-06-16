PORT ?= 8000
HOST ?= localhost

.PHONY: serve
serve:
	@echo "Serving on http://$(HOST):$(PORT)"
	php -S $(HOST):$(PORT) -t . dev-router.php

.PHONY: open
open: ## start server and open browser
	@( sleep 1 && open "http://$(HOST):$(PORT)" ) &
	@$(MAKE) serve
